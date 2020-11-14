from flask import Flask, jsonify, request
from flask_restful import Resource
from services.book_services import insert, get_all, get, update, delete

class Book(Resource):
    def get(self, author, title): 
        book = get(author, title)
        return book, 200
    
    def patch(self, author, title):
        new_data= request.get_json()
        update(author, title, new_data)
        return { }, 204
    
    def delete(self, author, title):
        delete(author, title)
        return { }, 204

class AllBooks(Resource):
    def post(self): 
        new_book = request.get_json()
        insert(new_book)
        return { "message": "created" }, 201
    
    def get(self):
        all_books = get_all()
        return all_books, 200
