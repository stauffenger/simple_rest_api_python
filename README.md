# REST API with Python
A REST API that works like a middleware for a library API, receiving a title and author and converting to a hash value to interact with the library API.

## What to expect?
This API will be built with python and the flask-restful, an extension of the framework flask, with the intention of showing the basic functionality of a REST API with python and how to use hash as an identification. Initially the API doesn't have the intention of demonstrate an interaction with any database, so this API will work like a simple middleware between a service that doesn't understand hash and a API that use hash as an items identification.

## How will the API work?
It'll format the data to pass for the library API.

## Services provided(path)
- Books('http://localhost:5000/books/'):
    - Register new book
    - Get all books
- A specific book('http://localhost:5000/book/author-name-separated-with-hyphen/title-separated-with-hyphen/'):
    - Update
    - Get
    - Delete

## Books insert/update model
```JSON
{
    "title": "book title",
    "author": "author name",
    "description": "short book description"
}
```

## How to start the project
```Shell
$ phyton app.py
```
or
```Shell
$ flask run
```

## Dependencies
- flask
- flask-restful
- flask-cors
- json
- werkzeug.exceptions
- hashlib

## References
- https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
- https://flask.palletsprojects.com/en/1.1.x/
- https://flask-restful.readthedocs.io/en/latest/
- https://werkzeug.palletsprojects.com/en/1.0.x/
- https://docs.python.org/2/library/hashlib.html
