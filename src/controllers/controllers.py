from flask import request
from libgen_api import LibgenSearch

def get_book_info():
    book_title = request.form.get("book-title")
    book_author = request.form.get("book-author")
    search_book(book_title, book_author)

def search_book(title, author):
    agent = LibgenSearch()
    query_filters = {"Extension": "epub", "Author": author}
    res = agent.search_title_filtered(title, query_filters, exact_match=False)

    filtered_book_results = [
            {
                "title" : item["Title"],
                "mirrors" : item["Mirror_1"]
            }

            for item in res
    ]

    for book_found in filtered_book_results:
        print(book_found['title'])
        print(book_found['mirrors'])
