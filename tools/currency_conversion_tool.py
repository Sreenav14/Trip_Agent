import os
from utils.currency_converter import CurrencyConverter
from typing import List, Dict, Any, Union
from langchain.tools import tool
from dotenv import load_dotenv



class CurrencyTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_serivce = CurrencyConverter(self.api_key)
        self.currency_tool_list = self.setup_tools()


    def setup_tools(self)->List:
        """ setup all tools for the currency convertor tool"""
        @tool
        def convert_currency(amount: float, from_currency:str, to_currency:str)-> float:
            """ Convert the amount from one currency to another."""
            return self.currency_serivce.convert(amount, from_currency, to_currency)
        return [convert_currency]