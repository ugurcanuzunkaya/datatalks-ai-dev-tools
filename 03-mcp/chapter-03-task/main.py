from fastmcp import FastMCP
from scraper import scrape

# Initialize the FastMCP server
mcp = FastMCP("Demo 🚀")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def scrape_website(url: str) -> str:
    """Scrape a website content using Jina Reader."""
    return scrape(url)


if __name__ == "__main__":
    mcp.run()
    import sys

    # If you must debug, print to stderr:
    print("Debug message", file=sys.stderr)
