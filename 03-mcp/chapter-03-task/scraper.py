import httpx


def scrape(url: str) -> str:
    """
    Scrape a URL using Jina Reader.

    Args:
        url: The URL to scrape.

    Returns:
        The text content of the scraped page.
    """
    jina_url = f"https://r.jina.ai/{url}"
    # Use follow_redirects=True to handle potential redirects,
    # though Jina usually returns direct content.
    # Using a timeout to prevent hanging.
    response = httpx.get(jina_url, follow_redirects=True, timeout=30.0)
    response.raise_for_status()
    return response.text
