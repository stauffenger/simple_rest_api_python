from database.simulated_library_api import add_new_book, get_all_books, get_book, update_book, delete_book
from werkzeug.exceptions import BadRequest, InternalServerError, Conflict, NotFound
from models.book import Book
import json

def insert(new_book):
    title_is_not_empty = new_book['title'] not in (None, " ", "")
    author_is_not_empty = new_book['author'] not in (None, " ", "")
    if title_is_not_empty:
        if author_is_not_empty:
            formmated_book = json.dumps(Book(new_book['title'], new_book['author'], new_book['description']).__dict__)
            book, http_status_code = add_new_book(formmated_book)
            if http_status_code == 409:
                error_message = "The book is already registered."
                raise Conflict(description=error_message)
            elif http_status_code != 201:
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
    if books:
        return books
    else:
        error_message = "No book found."
        raise NotFound(description=error_message)

def get(author, title):
    title_is_not_empty = title not in (None, " ", "")
    author_is_not_empty = author not in (None, " ", "")
    if title_is_not_empty:
        if author_is_not_empty:
            formatted_book = json.dumps(Book(title, author, description="").__dict__)
            book = get_book(formatted_book)
            if book:
                return book
            else:
                error_message = "The book was not found."
                raise NotFound(description=error_message)
        else:
            error_message = "The author is required."
            raise BadRequest(description=error_message)
    else:
        error_message = "The title is required."
        raise BadRequest(description=error_message)

def update(author, title, new_data):
    target_book = get(author, title)
    target_book_found = target_book
    if target_book_found:
        new_data_formatted = json.dumps(Book(new_data['title'], new_data['author'], new_data['description']).__dict__)
        target_book_formatted = json.dumps(target_book)
        response, http_status_code = update_book(target_book_formatted, new_data_formatted)
        if http_status_code != 204:
            error_message = "An internal error has occurred trying to update the book on the database."
            raise InternalServerError(description=error_message)
    else:
        error_message = "The book was not found."
        raise NotFound(description=error_message)

def delete(author, title):
    target_book = get(author, title)
    target_book_found = target_book
    if target_book_found:
        target_book_formatted = json.dumps(target_book)
        response, http_status_code = delete_book(target_book_formatted)
        if http_status_code != 204:
            error_message = "An internal error has occurred trying to delete the book on the database."
            raise InternalServerError(description=error_message)
    else:
        error_message = "The book was not found."
        raise NotFound(description=error_message)