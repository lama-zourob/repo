# Library Management API

## Description
This is a RESTful API for managing a library system. users can add, update, delete, and search for books.## Prerequisites
- Python 3.10 or higher
- Flask
- Postman (optional, for API testing)

## Setup and Run

1.Clone the repository:
   ```bash
   git clone https://github.com/lama-zourob/library-management-api.git
   cd library-management-api
   ```

2.Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3.Run the application:
   ```bash
   python app.py
   ```

4.Open your browser and navigate to:
   - Swagger documentation: `http://127.0.0.1:5000/api-docs`
   - API endpoints: `http://127.0.0.1:5000/`

## API Endpoints

### 1.Add a New Book
- **URL:** `/books/add`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "title": "Book Title",
    "author": "Author Name",
    "published_year": "2024",
    "isbn": "1234567890",
    "genre": "Fiction"
  }
  ```
- **Response:**
  - `302`: Redirects to the list of books.

---

### 2.List All Books
- **URL:** `/books/list`
- **Method:** `GET`
- **Response:**
  - A list of all books in JSON format.

---### 3.Search Books
- **URL:** `/books/search`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "query": "search_term"
  }
  ```
- **Response:**
  - A filtered list of books matching the query.

---

### 4.Update Book
- **URL:** `/update/<isbn>`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "title": "Updated Title",
    "author": "Updated Author"
  }
  ```
- **Response:**
  - `302`: Redirects to the list of books.

---

### 5.Delete Book
- **URL:** `/delete/<isbn>`
- **Method:** `POST`
- **Response:**
  - `302`: Redirects to the list of books.
## Postman Collection
A Postman collection is available for testing all endpoints.
