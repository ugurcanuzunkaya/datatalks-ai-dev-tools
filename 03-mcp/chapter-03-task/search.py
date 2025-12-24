import httpx
import zipfile
import io
import minsearch


def get_docs():
    """
    Downloads and prepares documentation files for indexing.
    """
    url = "https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip"
    docs = []

    print(f"Downloading {url}...")
    response = httpx.get(url, follow_redirects=True, timeout=30.0)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        for file_info in z.infolist():
            if file_info.filename.endswith((".md", ".mdx")):
                # Clean filename
                clean_name = file_info.filename.replace("fastmcp-main/", "")

                with z.open(file_info) as f:
                    content = f.read().decode("utf-8")

                docs.append({"filename": clean_name, "content": content})
    return docs


def build_index(docs):
    """
    Builds the search index using minsearch.
    """
    index = minsearch.Index(
        text_fields=["content", "filename"], keyword_fields=["filename"]
    )

    index.fit(docs)
    return index


def search(index, query):
    """
    Performs a search on the index.
    """
    boost = {"filename": 2.0}  # Boost filename relevance
    results = index.search(query=query, boost_dict=boost, num_results=1)
    return results


def main():
    docs = get_docs()
    print(f"Indexed {len(docs)} documents.")

    index = build_index(docs)

    query = "demo"
    print(f"Searching for '{query}'...")
    results = search(index, query)

    if results:
        print(f"First result filename: {results[0]['filename']}")
    else:
        print("No results found.")


if __name__ == "__main__":
    main()
