from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = {1: {"id": 1, "title": "ant", "author": "Bernard Werber"}}

# 엔드포인트 구현...
@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200, BookSchema(many=True))
    def get(self):
        return list(books.values())

    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_id = max(books.keys()) + 1 if books else 1
        new_data["id"] = new_id
        books[new_id] = new_data
        return books[new_id]



@book_blp.route("/<int:book_id>")
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        if book_id not in books:
            return abort(404, message= "Book not found.")
        return books[book_id]
    
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        if book_id not in books:
            return abort(404, message= "Book not found.")
        new_data["id"] = book_id
        books[book_id] = new_data
        return books[book_id]
    
    @book_blp.response(204)
    def delete(self, book_id):

        books.pop(book_id)
        return jsonify({"msg": "삭제"})
