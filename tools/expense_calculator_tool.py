from utils.expense_calculator import Calculator 
from typing import Any, Union, List, Dict
from langchain.tools import tool



class CalculatorTool():
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()
        
    def _setup_tools(self)-> List:
        """ setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night: str, total_days: float) -> float:
            """ Estimate the total hotel cost for the given price per night and total days.

            Accepts price_per_night as string (e.g. "$120") or numeric string and returns numeric total.
            """
            try:
                price = float(str(price_per_night).replace('$','').replace(',','').strip())
            except Exception:
                # If parsing fails, propagate a clear error message
                raise ValueError(f"Invalid price_per_night value: {price_per_night}")
            return self.calculator.multiply(price, float(total_days))
        @tool
        def estimate_total_expense(*costs: float)->float:
            """ Calculate total expense from the given costs."""
            return self.calculator.calculate_total(*costs)
        @tool
        def calculate_daily_budget(total_cost: float, days: int) -> float:
            """ Calculate daily budget from total cost and number of days."""
            return self.calculator.calculate_daily_budget(total_cost, days)
        return [estimate_total_hotel_cost,estimate_total_expense, calculate_daily_budget]
    