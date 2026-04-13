import sqlite3

DB_NAME = "bookstore.db"


def print_divider() -> None:
    print("\n" + "-" * 40)


def pause() -> None:
    input("\nPress Enter to continue...")


def print_menu() -> None:
    print_divider()
    print("Sci-Fi Bookstore Menu")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. Show available reads")
    print("9. Quit")


def welcome_screen() -> None:
    print_divider()
    print("Welcome to the Sci-Fi Bookstore")
    print("Your hub for classic sci-fi, cyberpunk, space opera, and hard science fiction.")
    pause()


def view_categories(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        "SELECT categoryId, categoryName, categoryImage FROM category ORDER BY categoryId"
    )
    rows = cursor.fetchall()

    print_divider()
    print("Categories")

    if rows:
        for row in rows:
            print(f"[{row[0]}] {row[1]} (image: {row[2]})")
    else:
        print("No categories found.")


def view_books(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT bookId, title, author, price, readNow
        FROM book
        ORDER BY title
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("All Books")

    if rows:
        for row in rows:
            read_label = "Available to read now" if row[4] == 1 else ""
            print(f"[{row[0]}] {row[1]} by {row[2]} — ${row[3]:.2f} {read_label}")
    else:
        print("No books found.")


def view_books_in_category(cursor: sqlite3.Cursor) -> None:
    category_id = input("Enter a category id: ").strip()

    cursor.execute(
        """
        SELECT book.bookId, book.title, book.author, book.price, category.categoryName
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE category.categoryId = ?
        ORDER BY book.title
        """,
        (category_id,)
    )
    rows = cursor.fetchall()

    print_divider()
    print("Books in Category")

    if rows:
        for row in rows:
            print(f"[{row[0]}] {row[1]} by {row[2]} — ${row[3]:.2f} (Category: {row[4]})")
    else:
        print("No books found for that category.")


def search_by_title(cursor: sqlite3.Cursor) -> None:
    keyword = input("Enter a title keyword: ").strip()

    cursor.execute(
        """
        SELECT bookId, title, author, price
        FROM book
        WHERE title LIKE ?
        ORDER BY title
        """,
        (f"%{keyword}%",)
    )
    rows = cursor.fetchall()

    print_divider()
    print("Matching Books")

    if rows:
        for row in rows:
            print(f"[{row[0]}] {row[1]} by {row[2]} — ${row[3]:.2f}")
    else:
        print("No books found matching that title.")


def add_book(cursor: sqlite3.Cursor) -> None:
    try:
        category_id = int(input("Enter category id: ").strip())
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        price = float(input("Enter price: ").strip())
        image = input("Enter image filename: ").strip()
        read_now = int(input("Enter readNow (0 or 1): ").strip())

        cursor.execute(
            """
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (category_id, title, author, isbn, price, image, read_now)
        )

        print_divider()
        print("Book added successfully.")

    except ValueError:
        print_divider()
        print("Invalid input. Please enter the correct data types.")
    except sqlite3.IntegrityError as error:
        print_divider()
        print("Database error:", error)


def update_price(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id: ").strip())
        new_price = float(input("Enter the new price: ").strip())

        cursor.execute(
            "UPDATE book SET price = ? WHERE bookId = ?",
            (new_price, book_id)
        )

        print_divider()
        if cursor.rowcount == 0:
            print("No book found with that id.")
        else:
            print("Price updated successfully.")

    except ValueError:
        print_divider()
        print("Invalid input. Please enter numeric values.")


def delete_book(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id to delete: ").strip())

        cursor.execute(
            "DELETE FROM book WHERE bookId = ?",
            (book_id,)
        )

        print_divider()
        if cursor.rowcount == 0:
            print("No book found with that id.")
        else:
            print("Book deleted successfully.")

    except ValueError:
        print_divider()
        print("Invalid input. Please enter a numeric book id.")


def view_read_now(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT book.bookId, book.title, book.author, book.price, category.categoryName
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE book.readNow = 1
        ORDER BY book.title
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("Available to Read Now")

    if rows:
        for row in rows:
            print(f"[{row[0]}] {row[1]} by {row[2]} — ${row[3]:.2f} (Category: {row[4]})")
    else:
        print("No books currently available to read now.")


def main() -> None:
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()

        welcome_screen()

        while True:
            print_menu()
            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                view_categories(cursor)
                pause()
            elif choice == "2":
                view_books(cursor)
                pause()
            elif choice == "3":
                view_books_in_category(cursor)
                pause()
            elif choice == "4":
                search_by_title(cursor)
                pause()
            elif choice == "5":
                add_book(cursor)
                pause()
            elif choice == "6":
                update_price(cursor)
                pause()
            elif choice == "7":
                delete_book(cursor)
                pause()
            elif choice == "8":
                view_read_now(cursor)
                pause()
            elif choice == "9":
                print_divider()
                print("Thanks for visiting the Sci-Fi Bookstore. Goodbye!")
                break
            else:
                print_divider()
                print("Invalid option. Please choose a number from the menu.")
                pause()


if __name__ == "__main__":
    main()

