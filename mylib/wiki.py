"""Helpers for searching Wikipedia content."""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError


def search_wikipedia(query, results=5):
    """Return a list of Wikipedia page title matches for a query."""
    return wikipedia.search(query, results=results)


def _get_best_match(query):
    """Return the first Wikipedia title match for a query."""
    matches = search_wikipedia(query, results=1)
    if not matches:
        raise ValueError(f"No Wikipedia match found for: {query}")
    return matches[0]


def summarize_wikipedia(query, sentences=2):
    """Return a short summary for the best Wikipedia match."""
    title = _get_best_match(query)

    try:
        summary = wikipedia.summary(title, sentences=sentences, auto_suggest=False)
    except DisambiguationError as error:
        raise ValueError(
            f"Wikipedia match for '{query}' is ambiguous: {', '.join(error.options[:5])}"
        ) from error
    except PageError as error:
        raise ValueError(f"Wikipedia page not found for: {title}") from error

    return {"title": title, "summary": summary}


def wikipedia_page_url(query):
    """Return the Wikipedia URL for the best match."""
    title = _get_best_match(query)

    try:
        page = wikipedia.page(title, auto_suggest=False)
    except DisambiguationError as error:
        raise ValueError(
            f"Wikipedia match for '{query}' is ambiguous: {', '.join(error.options[:5])}"
        ) from error
    except PageError as error:
        raise ValueError(f"Wikipedia page not found for: {title}") from error

    return {"title": page.title, "url": page.url}


def _example_usage():
    sample_query = "Python programming"
    print("Matches:", search_wikipedia(sample_query))
    print("Summary:", summarize_wikipedia(sample_query))
    print("URL:", wikipedia_page_url(sample_query))


if __name__ == "__main__":
    _example_usage()
