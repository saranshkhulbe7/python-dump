from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("Math")


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    _summary_
    Subtract two numbers
    """
    return a - b


@mcp.tool()
def divide(a: int, b: int) -> int:
    """
    _summary_
    Divide two numbers
    """
    if b == 0:
        return math.inf
    return a / b


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
