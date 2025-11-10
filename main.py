from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_document
from langchain_core.messages import HumanMessage
import os
import datetime
from dotenv import load_dotenv
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question:str
    
@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    try:
        print(f"Query received: {query.question}")
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()
        
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open ("my_graph.png","wb") as f:
            f.write(png_graph)
            
        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        messages = {"messages":[HumanMessage(content=query.question)]}
        print(f"Invoking graph with messages: {messages}")
        output = react_app.invoke(messages)
        print(f"Graph output: {output}")
        
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
            print(f"Final output extracted: {final_output[:200]}")
        else:
            final_output = str(output)
            print(f"Final output (as string): {final_output[:200]}")
            
        return {"answer":final_output}
    
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print(f"Error occurred: {str(e)}")
        print(tb)
        # Return the full traceback in the response to aid debugging in development.
        return JSONResponse(status_code=500, content={"error": str(e), "traceback": tb})
        