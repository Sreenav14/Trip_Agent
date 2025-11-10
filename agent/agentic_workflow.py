from typing import Any


from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import HumanMessage

from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.currency_conversion_tool import CurrencyTool
from tools.expense_calculator_tool import CalculatorTool
from tools.arthmatic_operation_tool import ArthmaticOperationTool


class GraphBuilder():
    
    def __init__(self,model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        self.tools = []
        
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyTool()
        
        self.tools.extend([* self.weather_tools.weather_tool_list, 
                           * self.place_search_tools.place_search_tool_list,
                           * self.calculator_tools.calculator_tool_list,
                           * self.currency_converter_tools.currency_tool_list])
        
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        
        self.graph = None
        self.system_prompt = SYSTEM_PROMPT
    
    def agent_function(self,state:MessagesState):
        "Main function Agent"
        messages = state["messages"]
        # If messages is a string (from the endpoint), convert it to HumanMessage
        if isinstance(messages, str):
            messages = [HumanMessage(content=messages)]
        elif isinstance(messages, list) and all(isinstance(m, str) for m in messages):
            messages = [HumanMessage(content=m) if isinstance(m, str) else m for m in messages]
        
        # Build the full message list with system prompt
        full_messages = [self.system_prompt] + messages
        response = self.llm_with_tools.invoke(full_messages)
        return {"messages":[response]}
    
    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        
        self.graph = graph_builder.compile()
        return self.graph
    
    def __call__(self):
        return self.build_graph()