from simulated_library_api import add_new_book, get_all_books
from werkzeug.exceptions import BadRequest, InternalServerError
from models import Book
import json

def insert(new_book):
    title_is_not_empty = new_book['title'] not in (None, " ", "")
    author_is_not_empty = new_book['author'] not in (None, " ", "")
    if title_is_not_empty:
        if author_is_not_empty:
            formmated_book = json.dumps(Book(new_book['title'], new_book['author'], new_book['description']).__dict__)
            book, http_status_code = add_new_book(formmated_book)
            if http_status_code != 201:
                error_message = "An internal error has occurred trying to register the book on the database."
                raise InternalServerError(description=error_message)
        else:
            error_message = "The author is required."
            raise BadRequest(description=error_message)
    else:
        error_message = "The title is required."
        raise BadRequest(description=error_message)

def get_all():
    books = get_all_books()
    return books
