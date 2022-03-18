from music.models import Book
books = Book.objects.filter(pub="清华大学出版社")
for book in books:
    print(book.title)