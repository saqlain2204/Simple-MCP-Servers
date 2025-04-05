from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="weather-server")

@mcp.tool()
def get_current_weather():
    pass

if __name__ == '__main__':
    mcp.run()