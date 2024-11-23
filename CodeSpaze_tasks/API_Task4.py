from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  
swagger = Swagger(app)
jwt = JWTManager(app)

# Sample in-memory data store
books = []


# Authentication Route
@app.route('/login', methods=['POST'])
def login():
    """
    User Login
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
        required:
          - username
          - password
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    username = request.json.get('username')
    password = request.json.get('password')

    
    if username == 'user' and password == 'password':
        token = create_access_token(identity={'username': username})
        return jsonify(access_token=token)
    return jsonify({"message": "Invalid credentials"}), 401


# CRUD Operations for Books
class Book(Resource):
    def get(self, book_id=None):
        """
        Get all books or a specific book
        ---
        tags:
          - Books
        parameters:
          - name: book_id
            in: path
            type: integer
            required: false
        responses:
          200:
            description: List of books or a single book
        """
        if book_id:
            book = next((book for book in books if book['id'] == book_id), None)
            return jsonify(book or {"message": "Book not found"})
        return jsonify(books)

    @jwt_required()
    def post(self):
        """
        Add a new book
        ---
        tags:
          - Books
        parameters:
          - in: body
            name: body
            schema:
              type: object
              properties:
                id:
                  type: integer
                title:
                  type: string
                author:
                  type: string
        responses:
          201:
            description: Book added
        """
        data = request.json
        books.append(data)
        return jsonify({"message": "Book added", "book": data}), 201

    @jwt_required()
    def put(self, book_id):
        """
        Update a book
        ---
        tags:
          - Books
        parameters:
          - name: book_id
            in: path
            type: integer
            required: true
          - in: body
            name: body
            schema:
              type: object
              properties:
                title:
                  type: string
                author:
                  type: string
        responses:
          200:
            description: Book updated
          404:
            description: Book not found
        """
        data = request.json
        book = next((book for book in books if book['id'] == book_id), None)
        if book:
            book.update(data)
            return jsonify({"message": "Book updated", "book": book})
        return jsonify({"message": "Book not found"}), 404

    @jwt_required()
    def delete(self, book_id):
        """
        Delete a book
        ---
        tags:
          - Books
        parameters:
          - name: book_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Book deleted
        """
        global books
        books = [book for book in books if book['id'] != book_id]
        return jsonify({"message": "Book deleted"})


# Adding Resources
api.add_resource(Book, "/books", "/books/<int:book_id>")


# Protected Route Example
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Protected Route
    ---
    tags:
      - Authentication
    responses:
      200:
        description: Access to protected route
    """
    return jsonify({"message": "This is a protected route"})


if __name__ == "__main__":
    app.run(debug=True)
