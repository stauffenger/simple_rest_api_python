from flask import Flask, request
from flask_restful import Resource
from book import get, update, delete
from all_books import insert, get_all
class Book(Resource):
    def get(self, author, title): 
        book = get(author, title)
        return book
    
    def patch(self, author, title):
        new_data= request.get_json()
        response = update(author, title, new_data)
        return response
    
    def delete(self, author, title):
        response = delete(author, title)
        return response

class AllBooks(Resource):
    def post(self): 
        new_book = request.get_json()
        response = insert(new_book)
        return response
    
    def get(self):
        all_books = get_all()
        return all_books
