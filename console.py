import pdb
from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Agatha", "Christie")
author_repository.save(author1)
author2 = Author("P.G", "Wodehouse")
author_repository.save(author2)

authors = author_repository.select_all()



book1 = Book("And Then There Were None", author1)
book_repository.save(book1)
book2 = Book("Five Little Pigs", author1)
book_repository.save(book2)
book3 = Book("The Inimitable Jeeves", author2)
book_repository.save(book3)

books = book_repository.select_all()

# pdb.set_trace()



