# create class structure

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self,book_name):
        self.books.append(book_name)
        print("Add sucessfully",{book_name})
    
    def show_books(self):
        if self.books:
            print("Available Books")
            for book in self.books:
                print({book})
            else:
                print("No availabe books")

# menu interface for user intersection
def main():
    library = Library()
    while True:
        print("\n====Library managaement  Menu ====")
        print("1: Add books")
        print("2: Show books" )
        print("3: Exit")
        
        choice = input("enter your choice (1-3)")


        if choice =='1':
            book = input("Enter book name to add")
            library.add_book(book)
        elif choice == '2':
            library.show_books()
        elif choice == '3':
            print("Exiting ......Goodby")
            break
        else:
            print("invalid choice please enter 1, 2, or 3")

if __name__ == "__main__":
    main()            
        
s=Library()
s.add_book("sssss")
s.show_books()
