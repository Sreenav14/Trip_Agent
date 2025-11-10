#!/usr/bin/env python
"""Test the /query endpoint without running the server"""

import sys
import traceback
from pydantic import BaseModel

print("=" * 60)
print("Testing /query endpoint logic")
print("=" * 60)

class QueryRequest(BaseModel):
    question: str

# Simulate the request
try:
    query = QueryRequest(question="Plan a trip to Goa")
    print(f"\n[OK] QueryRequest created: {query}")
except Exception as e:
    print(f"[FAIL] QueryRequest creation failed: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test GraphBuilder
print("\n[1] Testing GraphBuilder initialization...")
try:
    from agent.agentic_workflow import GraphBuilder
    graph = GraphBuilder(model_provider="groq")
    print("[OK] GraphBuilder initialized")
except Exception as e:
    print(f"[FAIL] GraphBuilder init failed: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test graph building
print("\n[2] Testing graph building...")
try:
    react_app = graph()
    print("[OK] Graph built successfully")
except Exception as e:
    print(f"[FAIL] Graph building failed: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test graph drawing
print("\n[3] Testing graph drawing (Mermaid PNG)...")
try:
    png_graph = react_app.get_graph().draw_mermaid_png()
    with open("test_graph.png", "wb") as f:
        f.write(png_graph)
    print("[OK] Graph PNG saved")
except Exception as e:
    print(f"[FAIL] Graph drawing failed: {e}")
    traceback.print_exc()
    sys.exit(1)

# Test invoking the graph
print("\n[4] Testing graph invocation...")
try:
    messages = {"messages": [query.question]}
    print(f"   Input: {messages}")
    output = react_app.invoke(messages)
    print("[OK] Graph invocation successful")
    print(f"   Output type: {type(output)}")
    print(f"   Output keys: {output.keys() if isinstance(output, dict) else 'N/A'}")
    
    # Test extracting the final output
    if isinstance(output, dict) and "messages" in output:
        final_output = output["messages"][-1].content
        print(f"[OK] Final output extracted: {final_output[:100]}...")
    else:
        final_output = str(output)
        print(f"[OK] Final output (as string): {final_output[:100]}...")
        
except Exception as e:
    print(f"[FAIL] Graph invocation failed: {e}")
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("All tests passed! Endpoint should work correctly.")
print("=" * 60)
