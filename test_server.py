from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="calculator")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers and return the result

    Args:
        a: first number to add
        b: second number to add
    
    Returns:
        The addition of 2 numbers a and b
    
    """
    return a + b

@mcp.tool()
def area_of_triangle(b: int, h: int) -> float:
    """
    Calculate the area of the height

    Args:
        b: Base of the triangle
        h: Height of the traingle
    
    Returns:
        The area of the traiangle based on the base and the height
    
    """
    return (b*h/2)

@mcp.tool()
def get_unique_number() -> int:
    import random
    """
    Returns a unique number

    Args:
        None
    
    Return:
        An integer which is a unique number
    """
    return random.randint(1, 100)

if __name__ == '__main__':
    print("Server is starting")
    mcp.run()