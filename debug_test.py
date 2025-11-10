#!/usr/bin/env python
"""Debug script to test imports and initialization"""

import sys
import traceback

print("=" * 60)
print("Testing imports and initialization")
print("=" * 60)

# Test 1: Import tools
print("\n[1] Testing tool imports...")
try:
    from tools.weather_info_tool import WeatherInfoTool
    print("✓ WeatherInfoTool imported")
except Exception as e:
    print(f"✗ WeatherInfoTool failed: {e}")
    traceback.print_exc()

try:
    from tools.place_search_tool import PlaceSearchTool
    print("✓ PlaceSearchTool imported")
except Exception as e:
    print(f"✗ PlaceSearchTool failed: {e}")
    traceback.print_exc()

try:
    from tools.currency_conversion_tool import CurrencyTool
    print("✓ CurrencyTool imported")
except Exception as e:
    print(f"✗ CurrencyTool failed: {e}")
    traceback.print_exc()

try:
    from tools.expense_calculator_tool import CalculatorTool
    print("✓ CalculatorTool imported")
except Exception as e:
    print(f"✗ CalculatorTool failed: {e}")
    traceback.print_exc()

try:
    from tools.arthmatic_operation_tool import ArthmaticOperationTool
    print("✓ ArthmaticOperationTool imported")
except Exception as e:
    print(f"✗ ArthmaticOperationTool failed: {e}")
    traceback.print_exc()

# Test 2: Initialize tools
print("\n[2] Testing tool initialization...")
try:
    weather_tools = WeatherInfoTool()
    print(f"✓ WeatherInfoTool initialized - has {len(weather_tools.weather_tool_list)} tools")
except Exception as e:
    print(f"✗ WeatherInfoTool init failed: {e}")
    traceback.print_exc()

try:
    place_tools = PlaceSearchTool()
    print(f"✓ PlaceSearchTool initialized - has {len(place_tools.place_search_tool_list)} tools")
except Exception as e:
    print(f"✗ PlaceSearchTool init failed: {e}")
    traceback.print_exc()

try:
    currency_tools = CurrencyTool()
    print(f"✓ CurrencyTool initialized - has {len(currency_tools.currency_tool_list)} tools")
except Exception as e:
    print(f"✗ CurrencyTool init failed: {e}")
    traceback.print_exc()

try:
    calculator_tools = CalculatorTool()
    print(f"✓ CalculatorTool initialized - has {len(calculator_tools.calculator_tool_list)} tools")
except Exception as e:
    print(f"✗ CalculatorTool init failed: {e}")
    traceback.print_exc()

try:
    arithmetic_tools = ArthmaticOperationTool()
    print(f"✓ ArthmaticOperationTool initialized - has {len(arithmetic_tools.arithmetic_tool_list)} tools")
except Exception as e:
    print(f"✗ ArthmaticOperationTool init failed: {e}")
    traceback.print_exc()

# Test 3: Test GraphBuilder
print("\n[3] Testing GraphBuilder initialization...")
try:
    from agent.agentic_workflow import GraphBuilder
    graph = GraphBuilder(model_provider="groq")
    print("✓ GraphBuilder initialized")
except Exception as e:
    print(f"✗ GraphBuilder init failed: {e}")
    traceback.print_exc()

print("\n" + "=" * 60)
print("Debug test complete")
print("=" * 60)
