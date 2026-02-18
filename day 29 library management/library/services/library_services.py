from library.models import Book
class libraryServices():
    def __init__(self):
        self.books={}
    def addbook(self,book_name,author_name):
        # Creating book object
        new_book_id=len(self.books)
        book = Book(book_id=new_book_id,title=book_name,author=author_name)
        # adding new book object
        self.books[new_book_id]=book
        return f"{book_name} added and book it is {new_book_id}"
        
    def Remove_book(self,bookid:int):
        if bookid in self.books:
            book_obj=self.books[booksid]
            book_obj.is_available=False
            pass
    # def Add_user():
    #     pass
    # def Remove_user():
    #       pass
    def Borrow_book(self,bookid:int):
        if bookid in self.books:
            # Make book is_available false
            book_obj=self.books[bookid]
            book_obj.is_available=False
            return f'Book is borrowed successfully'
        return "Book is not found"
    def Return_book():
        pass
    def Get_avail_book():
        pass