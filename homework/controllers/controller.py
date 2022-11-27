from flask import render_template, request
from app import app
from models.book import Book
from models.all_books import books, add_book, remove_book, find_by_title

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/books')
def bookpage():
    return render_template('books.html', books=books)

@app.route('/donate')
def donatepage():
    return render_template('donate.html')

@app.route('/donate', methods=['POST'])
def add_form():
    form_data = request.form
    title = form_data['title']
    author = form_data['author']
    genre = form_data['genre']
    available = 'available' in form_data
    donate_book = Book(title, author, genre, available)
    add_book(donate_book)
    return render_template('books.html', books=books)

@app.route('/remove')
def remove_page():
    return render_template('remove.html', books=books)


@app.route('/remove', methods=['POST'])
def remove_form():
    form_data = request.form
    title = form_data['title']
    remove_book(title)
    return render_template('books.html', books=books)