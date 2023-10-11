from flask import Flask,jsonify,request
import requests

app= Flask(__name__)

books=[
    {"id": 1,"title":"Book 1","author": "Author 1"},
    {"id": 2,"title":"Book 2","author": "Author 2"},
    {"id": 3,"title":"Book 3","author": "Author 3"}
]

#Get all bookspi
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify({'books': books})

#Get a specific book by ID
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']== book_id:
            return book

    return jsonify({'error':'Book not found'})

#Creating a book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book={'id':len(books)+1,'title':request.json['title'],'author':request.json['author']}
    books.append(new_book)
    return jsonify({'message': 'Book created successfully', 'book': new_book})

#update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data=request.get_json()
    for book in books:
        if book['id'] == book_id:
            book['title'] = data.get('title', book['title'])
            book['author'] = data.get('author', book['author'])
            return jsonify({'message': 'Book updated successfully', 'book': book})
        return jsonify({'error': 'Book not found'})

#delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message': 'Book deleted successfully', 'book': book})
    return jsonify({'error': 'Book not found'})

#run the flask app
if __name__ == '__main__':
    app.run(debug=True)