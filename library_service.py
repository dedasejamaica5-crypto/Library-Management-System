"""Library Service class for managing books, members, and loans."""

from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """Service layer for managing library operations."""

    def __init__(self):
        """Initialize the LibraryService."""
        self._books = {}  # Dictionary: book_id -> Book
        self._members = {}  # Dictionary: member_id -> Member
        self._loans = []  # List of Loan objects
        self._loan_counter = 0  # Counter for generating loan IDs

    # ==================== BOOK MANAGEMENT ====================

    def add_book(self, book_id, title, author):
        """
        Add a new book to the library.

        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book

        Returns:
            Book: The newly created book object
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book

    def view_books(self):
        """
        Get all books in the library.

        Returns:
            list: List of all Book objects
        """
        return list(self._books.values())

    # ==================== MEMBER MANAGEMENT ====================

    def register_member(self, member_id, name, email):
        """
        Register a new member in the library.

        Args:
            member_id (str): Unique identifier for the member
            name (str): Full name of the member
            email (str): Email address of the member

        Returns:
            Member: The newly created member object
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member

    def view_members(self):
        """
        Get all registered members.

        Returns:
            list: List of all Member objects
        """
        return list(self._members.values())

    # ==================== LOAN MANAGEMENT ====================

    def borrow_book(self, book_id, member_id):
        """
        Borrow a book for a member.

        Args:
            book_id (str): ID of the book to borrow
            member_id (str): ID of the member borrowing the book

        Returns:
            Loan: The newly created loan object

        Raises:
            BookNotFoundError: If book is not found
            MemberNotFoundError: If member is not found
            BookUnavailableError: If book is already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")

        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")

        # Check if book is available
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")

        # Mark book as borrowed
        book.borrow()

        # Create and store loan
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)

        return loan

    def return_book(self, loan_id):
        """
        Return a borrowed book.

        Args:
            loan_id (str): ID of the loan to close

        Returns:
            Loan: The closed loan object

        Raises:
            LoanNotFoundError: If loan is not found
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break

        if loan is None:
            raise LoanNotFoundError(f"Loan {loan_id} not found.")

        # Mark book as available
        loan.book.return_book()

        # Close the loan
        loan.close_loan()

        return loan

    def view_loans(self):
        """
        Get all loans.

        Returns:
            list: List of all Loan objects
        """
        return list(self._loans)
