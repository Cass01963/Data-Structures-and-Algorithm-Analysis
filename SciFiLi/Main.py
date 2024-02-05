# Final Program
# Christian Carranza
# Sources include:
# https://realpython.com/python-hash-table/, https://intellipaat.com/blog/what-is-hash-table/
# https://www.scaler.com/topics/binary-search-tree-python/, https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# https://www.tutorialspoint.com/heap-queue-or-heapq-in-python, https://stackoverflow.com/questions/12749622/understanding-how-to-create-a-heap-in-python
# https://www.geeksforgeeks.org/python-program-for-merge-sort/
# https://www.geeksforgeeks.org/stack-and-queues-in-python/, https://realpython.com/queue-in-python/
# https://chat.openai.com/, previous programs throught this course, CSC 210, CSC 102

from queue import Queue
import heapq

# Book class that creates the book by title, author, checked in status, and priorty
class Book:
    def __init__(self, title, author, checked, priority):
        self.title = title
        self.author = author
        self.checked = checked
        self.priority = priority
    
    # less than method for rescue class
    def __lt__(self, other):
        return self.priority < other.priority
    
    # print str method for rescue class
    def __str__(self):
        return f"{self.title} by {self.author}\n  Priority #: {self.priority}"
    
# Node class to create the Binary Search Tree
class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

# Internally Storing book list into a hash table (TASK 1) and TASK 5 combined
class HashTable:
    # Storing book list into a hash table
    # A hash table would provide constant-time access to the books and allow for efficient
    # searching, insertion, and deletion of books based on their unique keys.
    # The keys could be the book titles, which would allow for easy alphabetical sorting
    # when outputting the books at the end of the day.
    def __init__(self):
        self.books = {}
        
    def insert(self, book):
        self.books[book.title] = book
        
    def get_book(self, title):
        return self.books.get(title)
    
    # TASK 5
    # Using a merge sort would allow for efficient sorting of the books based on their titles in alphabetical order.
    def output(self):
        sorted_titles = self._merge_sort(list(self.books.keys()))
        for title in sorted_titles:
            book = self.get_book(title)
            print(f"{book.title} by {book.author}, {book.checked}, {book.priority}")
    
    # MERGE SORT
    # The merge sort algorithm has a time complexity of O(n log n),
    # which is efficient enough for the number of books that would be stored in the library.
    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = self._merge_sort(left)
        right = self._merge_sort(right)
        return self._merge(left, right)
    
    def _merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged

# TASK 2
# Using a Binary Search Tree to search books based on titles or authors
# A binary search tree would allow for efficient and faster searching 
# The binary search tree requires a node class to indicate parents and children
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, book):
        new_node = Node(book)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if book.title < current_node.book.title:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                elif book.title > current_node.book.title:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.book.append(book)
                     
    def search_by_title(self, title):
        current_node = self.root
        while current_node is not None:
            if title == current_node.book.title:
                return current_node.book
            elif title < current_node.book.title:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    """
    def search_by_author(self, author):
        books = []
        current_node = self.root
        self._search_by_author_helper(current_node, author, books)
        return books

    def _search_by_author_helper(self, node, author, books):
        if node is None:
            return
        self._search_by_author_helper(node.left, author, books)
        if node.book.author == author:
            books.append(node.book)
        self._search_by_author_helper(node.right, author, books)
    """
    
# TASK 3
# Queue
# This would allow for first- in, first out (FIFO)
# order of books to be processed, similar to a real-life return process
class Library:
    def __init__(self):
        self.book_queue = Queue()
    
    def check_book(self, book):
        self.book_queue.put(book)
    """
    def check_out_book(self):
        if self.book_queue.empty():
            print('No books available to check out.')
            return

        book = self.book_queue.get()
        book.checked = 0
        print(f'{book.title} by {book.author} has been checked out.')
    """
    # method to check book in based on the user's input
    def check_in_book(self):
        title = input('Enter the title of the book being returned: ')
        found_book = False
        # stacks input on top of queue
        for book in list(self.book_queue.queue):
            if book.title.lower() == title.lower():
                # checked in book = 1 in txt file
                book.checked = 1
                found_book = True
                print(f'{book.title} by {book.author} has been checked in.')
                break
        # provides error message if book is not found in the library
        if not found_book:
            print(f'{title} was not found in the library.')

# TASK 4
# Heap Queue
# The heap queue would be based on the book's priority value, with lower values having higher priority.
# The heap queue would allow for easy access to the books in order of importance. 
class Rescue:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    # Only books that are checked in would be added to the heap queue.    
    def print_rescue_list(self):
        rescue_list = []
        for book in self.books:
            # heap queue pushes checked out books out of the rescue list
            if book.checked:
                heapq.heappush(rescue_list, book)
        print("Books that need to be rescued:")
        while rescue_list:
            # heap que pops checked in books and orders them based on priority number
            book = heapq.heappop(rescue_list)
            print(str(book))


#############
### MAIN ####
#############

if __name__ == '__main__':
    # assigning var to each class
    ht = HashTable()
    bst = BinarySearchTree()
    rcue = Rescue()
    lib = Library()
    
    # opens and reads txt file
    with open("SciFiLiBooks.txt", "r") as file:
        for line in file:
            fields = line.strip().split(',')
            # assigning placement values, as well as defining checked and priority as int
            title = fields[0]
            author = fields[1]
            checked = int(fields[2])
            priority = int(fields[3])
            # creating the book
            book = Book(title, author, checked, priority)
            # inserting book into each different class method
            ht.insert(book)
            bst.insert(book)
            lib.check_book(book)
            rcue.add_book(book)
    
    # Welcome Statement
    print("Welcome to Dr. Lori's Library Website!")
    print("Here you will find books that only pertain to her interest and such.")
    print("All of our books have been stored internally through our database using a HashTable.")
    
    # loops menu until the user quits (indicated in instructions)
    done = False
    while done == False:
        print("\nTo begin any tasks type in the number:")
        print("1 (Search book by title or author.)")
        print("2 (Check In or Check Out books/return process)")
        print("3 (Operation rescue)")
        print("4 (Quit Website)")
        numbers = int(input('\nType in number of choice: '))
        if numbers == 1:
            #TASK 2
            print("\nSearch book by author is offline, having technical difficulties :(")
            book = bst.search_by_title(input('\nSearch book by typing in the title: '))
            if book:
                print('Found book:', book.title, 'by', book.author, book.checked, book.priority)
            else:
                print('Book not found.')

            """
            # Search for all books by an author
            books = bst.search_by_author(input('Search book by typing in the author: '))
            if books:
                print('Found', len(books), 'books by', author, ':')
                for book in books:
                    print(book.title, book.author, book.checked, book.priority)
            else:
                print('No books found by', author)
            """
            
        elif numbers == 2:
            # TASK 3
            print('\n1. Check out a book is offline, having technical difficulites :(\n2. Check in a book')
            choice = input('Enter your # of choice: ')
            """
            if choice == '1':
                lib.check_out_book()
            """

            if choice == '2':
                lib.check_in_book()
            
            else:
                print('Invalid choice. Please try again.')
        
        elif numbers == 3:
            #TASK 4
            print("\nThis is a list of all the checked in books that need to be rescued in case of a fire.")
            print("Key Note: Books are ordered by priority.")
            rcue.print_rescue_list()
        
        else:
            # TASK 5
            print("\nYou have quit out of the website.\nHere we will output all books (alphabetically by title) and if they’re checked in or out.")
            print("Key Note: 1 = Checked In, 0 = Checked Out")
            print("Output into a different file is offline, having technical difficulties :(")
            ht.output()
            done = True
            quit()
    