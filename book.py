from simulated_library_api import get_book, update_book, delete_book
from models import Book
from errors import BadRequest, InternalServerError, NotFound
import json

def get(author, title):
    title_is_not_empty = title not in (None, " ", "")
    author_is_not_empty = author not in (None, " ", "")
    if title_is_not_empty:
        if author_is_not_empty:
            try:
                formatted_book = json.dumps(Book(title, author, description="").__dict__)
                book, http_status_code = get_book(formatted_book)
            except:
                error_message = "An internal error has occurred trying to get the book on the database."
                raise InternalServerError(error_message)
        else:
            error_message = "The author is required."
            raise BadRequest(error_message)
    else:
        error_message = "The title is required."
        raise BadRequest(error_message)
    return book, http_status_code

def update(author, title, new_data):
    target_book, http_status_code = get(author, title)
    target_book_found = target_book and http_status_code == 200
    if target_book_found:
        new_data_formatted = json.dumps(Book(new_data['title'], new_data['author'], new_data['description']).__dict__)
        response = update_book(target_book, new_data_formatted)
    else:
        error_message = "The book was not found."
        raise NotFound(error_message)
    return response

def delete(author, title):
    target_book, http_status_code = get(author, title)
    target_book_found = target_book and http_status_code == 200
    if target_book_found:
        response = delete_book(target_book)
    else:
        error_message = "The book was not found."
        raise NotFound(error_message)
    return response