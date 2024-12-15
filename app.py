from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)

DATA_FILE = "data.json"

def load_books():
    """Load books from data.json."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_books(books):
    """Save books to data.json."""
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)


SWAGGER_URL = '/api-docs' 
API_URL = '/static/swagger.json'  


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Library Management API"
    }
)


app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books/list", methods=["GET"])
def list_books():
    books = load_books()
    return render_template("list_books.html", books=books)

@app.route("/books/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        published_year = request.form.get("published_year")
        isbn = request.form.get("isbn")
        genre = request.form.get("genre")

        if not (title and author and published_year and isbn):
            return "All fields except genre are required!", 400

        books = load_books()
        books.append({
            "title": title,
            "author": author,
            "published_year": published_year,
            "isbn": isbn,
            "genre": genre
        })
        save_books(books)
        return redirect(url_for("list_books"))

    return render_template("add_book.html")

@app.route("/update/<string:isbn>", methods=["GET", "POST"])
def update_book(isbn):
    books = load_books()
    book = next((b for b in books if b["isbn"] == isbn), None)
    if not book:
        return "Book not found", 404

    if request.method == "POST":
        book["title"] = request.form.get("title", book["title"])
        book["author"] = request.form.get("author", book["author"])
        book["published_year"] = request.form.get("published_year", book["published_year"])
        book["genre"] = request.form.get("genre", book["genre"])
        save_books(books)
        return redirect(url_for("list_books"))

    return render_template("update_book.html", book=book)

@app.route("/delete/<string:isbn>", methods=["POST"])
def delete_book(isbn):
    books = load_books()
    books = [b for b in books if b["isbn"] != isbn]
    save_books(books)
    return redirect(url_for("list_books"))

@app.route("/books/search", methods=["GET", "POST"])
def search_books():
    """Search books by title, author, or genre."""
    books = None
    if request.method == "POST":
        query = request.form.get("query", "").lower()
        all_books = load_books()
        
        books = [
            book for book in all_books
            if query in book["title"].lower() or
               query in book["author"].lower() or
               query in (book.get("genre", "") or "").lower()
        ]
    
    return render_template("search.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
