# Model Context Protocol (MCP) Server Task

This project builds a **Model Context Protocol (MCP)** server using `fastmcp` as part of the AI Dev Tools Zoomcamp (Module 3).

## Features

The server (`main.py`) exposes the following tools:

1.  **`add(a, b)`**: A simple math tool to add two integers.
2.  **`scrape_website(url)`**: Scrapes the text content of a given URL using Jina Reader (via `scraper.py`).

Configuration and search utilities are also included:

*   **`scraper.py`**: Helper module for web scraping using `httpx`.
*   **`search.py`**: A standalone script (CLI) that:
    *   Downloads the `fastmcp` repository documentation.
    *   Indexes MD/MDX files using `minsearch`.
    *   Performs a search query (demo: searches for "demo").

## Setup

1.  **Install dependencies**:
    ```bash
    uv sync
    ```
    (Or `uv add fastmcp httpx minsearch`)

2.  **Run the Server**:
    ```bash
    uv run main.py
    ```

3.  **Run the Search Demo**:
    ```bash
    uv run search.py
    ```

## Project Structure

*   `main.py`: The entry point for the MCP server.
*   `scraper.py`: Logic for the scraping tool.
*   `search.py`: Logic for downloading, indexing, and searching docs.
*   `test_scrape.py`: A test script to verify scraping functionality.

## Usage with AI Clients

To use this server with Claude Desktop or Cursor, configure your client to run:

```json
{
  "mcpServers": {
    "datatalks-demo": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/datatalks-ai-dev-tools/03-mcp/chapter-03-task",
        "run",
        "--quiet",
        "main.py"
      ]
    }
  }
}
```
