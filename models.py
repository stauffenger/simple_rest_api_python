class Book:
    def __init__(self, title, author, description):
        self.title = title.replace("-", " ").upper()
        self.author = author.replace("-", " ").upper()
        self.description = description