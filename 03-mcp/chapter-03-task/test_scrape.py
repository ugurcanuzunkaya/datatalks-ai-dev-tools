from scraper import scrape


def main():
    target_url = "https://github.com/alexeygrigorev/minsearch"
    print(f"Scraping {target_url}...")
    try:
        content = scrape(target_url)
        print(f"Success! Content length: {len(content)}")
    except Exception as e:
        print(f"Error scraping: {e}")


if __name__ == "__main__":
    main()
