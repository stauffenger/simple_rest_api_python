from flask import Flask, jsonify, request
from flask_restful import Resource
from book import get, update, delete
from all_books import insert, get_all
class Book(Resource):
    def get(self, target_author, target_title): 
        book = get(target_author, target_title)
        return book
    
    def patch(self, target_author, target_title):
        new_data= request.get_json()
        response = update(target_author, target_title, new_data)
        return response
    
    def delete(self, target_author, target_title):
        response = delete(target_author, target_title)
        return response

class AllBooks(Resource):
    def post(self): 
        new_book = request.get_json()
        response = insert(new_book)
        return response
    
    def get(self):
        all_books = get_all()
        return all_books
