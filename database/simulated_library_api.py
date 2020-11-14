import json

def check_if_empty(target_file):
    target_file.seek(0) 
    first_char = target_file.read(1)
    if not first_char:
        return True
    else:
        target_file.seek(0) 
        return False

def add_new_book(new_book):
    book_already_exists = get_book(new_book)
    if book_already_exists:
            http_status_code = 409
            message = { "message": "The book is already registered." }
    else:
        books = get_all_books()
        new_book_formatted = json.loads(new_book)
        books.append(new_book_formatted)
        with open("./database/my_library.json", "w+") as library:
            json.dump(books, library, indent=4)
            http_status_code = 201
            message = { "message": "Created." }
        library.close()
    return message, http_status_code

def get_all_books():
    with open("./database/my_library.json") as library:
        file_is_empty = check_if_empty(library)
        books_found = False
        if not file_is_empty:
            books_found = json.load(library)
    library.close()
    return books_found

def update_book(target_book, new_data):
    book_found = get_book(target_book)
    if book_found:
        new_data_formatted = json.loads(new_data)
        books = get_all_books()
        for book in books:
            if book['id'] == book_found['id']:
                index = books.index(book)
                books[index] = new_data_formatted
        with open("./database/my_library.json", "w+") as library:
            json.dump(books, library, indent=4)
            http_status_code = 204
        library.close()
    else:
        http_status_code = 404
    return {}, http_status_code

def get_book(target_book):
    with open("./database/my_library.json") as library:
        file_is_empty = check_if_empty(library)
        target_book_formatted = json.loads(target_book)
        book_found = False
        if not file_is_empty:
            books = json.load(library)
            for book in books:
                if book['id'] == target_book_formatted['id']:
                    book_found = book
    library.close()
    return book_found

def delete_book(target_book):
    book_found = get_book(target_book)
    if book_found:
        books = get_all_books()
        books.remove(book_found)
        with open("./database/my_library.json", "w+") as library:
            json.dump(books, library, indent=4)
            http_status_code = 204
        library.close()
    else:
        http_status_code = 404
    return {}, http_status_code
