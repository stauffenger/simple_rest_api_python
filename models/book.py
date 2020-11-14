import hashlib

class Book:
    def __init__(self, title, author, description):
        self.title = title.replace("-", " ").upper()
        self.author = author.replace("-", " ").upper()
        hash_key = self.title + self.author
        self.id = hashlib.sha256(hash_key.encode('utf-8')).hexdigest()
        self.description = description
