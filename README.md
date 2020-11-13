# REST API with Python
A REST API that works like a middleware for a library API, receiving a title and author and converting to a hash value to interact with the library API.

## What to expect?
This API will be built with python and the flask-restful, an extension of the framework flask, with the intention of show the basic functionality of a REST API with python and how to use hash as an identification. Initially the API don't have the intention of demonstrate an interaction with any database, so this API will work like a simple middleware between a service that don't understand hash and a API that usa hash as a items identification.

## How will the API work?
It'll format the data to pass for the library API.

## Services provided
- Books:
    - Create
    - Read
    - Update
    - Delete

## Books model
```JSON
{
    "title": "book title",
    "author": "author name",
    "description": "short book description"
}
```

## How to start the project

## Dependencies

## References
