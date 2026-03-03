#!/usr/bin/env python3
"""Simple arxiv search script using the public API."""

import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import argparse


NS = "http://www.w3.org/2005/Atom"


def search(query: str, max_results: int = 10, sort_by: str = "relevance") -> list[dict]:
    params = urllib.parse.urlencode({
        "search_query": query,
        "max_results": max_results,
        "sortBy": sort_by,          # relevance | lastUpdatedDate | submittedDate
        "sortOrder": "descending",
    })
    url = f"http://export.arxiv.org/api/query?{params}"
    with urllib.request.urlopen(url) as resp:
        data = resp.read()

    root = ET.fromstring(data)
    results = []
    for entry in root.findall(f"{{{NS}}}entry"):
        arxiv_id = entry.findtext(f"{{{NS}}}id", "").split("/abs/")[-1]
        title = entry.findtext(f"{{{NS}}}title", "").strip().replace("\n", " ")
        summary = entry.findtext(f"{{{NS}}}summary", "").strip().replace("\n", " ")
        published = entry.findtext(f"{{{NS}}}published", "")[:10]
        authors = [a.findtext(f"{{{NS}}}name", "") for a in entry.findall(f"{{{NS}}}author")]
        results.append({
            "id": arxiv_id,
            "title": title,
            "authors": authors,
            "published": published,
            "abstract": summary,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
        })
    return results


def print_results(results: list[dict], show_abstract: bool = False) -> None:
    for i, r in enumerate(results, 1):
        print(f"\n[{i}] {r['title']}")
        print(f"    {r['published']}  |  {', '.join(r['authors'][:3])}{'...' if len(r['authors']) > 3 else ''}")
        print(f"    {r['url']}")
        if show_abstract:
            print(f"    Abstract: {r['abstract'][:300]}...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search arxiv papers")
    parser.add_argument("query", help="Search query (arxiv query syntax supported)")
    parser.add_argument("-n", "--num", type=int, default=10, help="Number of results (default: 10)")
    parser.add_argument("-s", "--sort", choices=["relevance", "lastUpdatedDate", "submittedDate"],
                        default="relevance", help="Sort order (default: relevance)")
    parser.add_argument("-a", "--abstract", action="store_true", help="Show abstracts")
    args = parser.parse_args()

    results = search(args.query, max_results=args.num, sort_by=args.sort)
    print(f"\nFound {len(results)} results for: {args.query!r}")
    print_results(results, show_abstract=args.abstract)
