from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator MCP")

@mcp.tool
def add(a: float, b: float)->float:
    return a + b

@mcp.tool
def random_number(min_val: int, max_val: int)->int:
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_resourse()->str:
    info = {
        "name": "Simple Calculator MCP",
        "version": "1.0",
        "description": "A simple MCP that provides addition and random number generation tools.",
        "tools": ["add", "random_number"],
        "author": "M Shahzaib"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport = "http", host = "0.0.0.0", port = 8000)