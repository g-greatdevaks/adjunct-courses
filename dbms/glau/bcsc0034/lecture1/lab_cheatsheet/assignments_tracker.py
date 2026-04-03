import os
import mysql.connector


def establish_connection():
    """
    Establishes a connection to the MySQL Server using environment variables
    or default lab credentials.
    """
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "127.0.0.1"),
            user=os.environ.get("DB_USER", "student"),
            password=os.environ.get("MYSQL_DB_PASSWORD", "dummy_password"),
            database=os.environ.get("DB_NAME", "student_tasks"),
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None


def add_assignment(connection, title, subject, due_date):
    """
    Inserts a new assignment record into the database using parameterized queries.
    """
    query = "INSERT INTO assignments (title, subject, due_date) VALUES (%s, %s, %s)"
    try:
        cursor = connection.cursor()
        cursor.execute(query, (title, subject, due_date))
        connection.commit()
        print(f"\n[Success] Assignment '{title}' added.")
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"\n[Error] Failed to add assignment: {err}")
    finally:
        cursor.close()


def view_assignments(connection):
    """
    Retrieves and displays all assignment records.
    """
    query = (
        "SELECT assignment_id, title, subject, due_date, is_completed FROM assignments"
    )
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()

        if not records:
            print("\nNo assignments found.")
            return

        print(
            f"\n{'ID':<5} | {'Title':<30} | {'Subject':<15} | {'Due Date':<12} | {'Status':<10}"
        )
        print("-" * 80)
        for row in records:
            status = "Completed" if row[4] else "Pending"
            print(
                f"{row[0]:<5} | {row[1]:<30} | {row[2]:<15} | {str(row[3]):<12} | {status:<10}"
            )
    except mysql.connector.Error as err:
        print(f"\n[Error] Failed to retrieve assignments: {err}")
    finally:
        cursor.close()


def complete_assignment(connection, assignment_id):
    """
    Marks an assignment as completed.
    """
    query = "UPDATE assignments SET is_completed = TRUE WHERE assignment_id = %s"
    try:
        cursor = connection.cursor()
        cursor.execute(query, (assignment_id,))
        connection.commit()
        print(f"\n[Success] Assignment ID {assignment_id} marked as completed.")
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"\n[Error] Failed to update assignment: {err}")
    finally:
        cursor.close()


def remove_assignment(connection, assignment_id):
    """
    Deletes an assignment record from the database.
    """
    query = "DELETE FROM assignments WHERE assignment_id = %s"
    try:
        cursor = connection.cursor()
        cursor.execute(query, (assignment_id,))
        connection.commit()
        print(f"\n[Success] Assignment ID {assignment_id} removed.")
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"\n[Error] Failed to remove assignment: {err}")
    finally:
        cursor.close()


def view_assignments_sorted(connection):
    """
    Retrieves and displays assignments sorted by due date.
    """
    query = (
        "SELECT assignment_id, title, due_date FROM assignments ORDER BY due_date ASC"
    )
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()

        print("\n--- Assignments Sorted by Due Date (Ascending) ---")
        for row in records:
            print(f"ID: {row[0]} | Title: {row[1]} | Due: {row[2]}")
    except mysql.connector.Error as err:
        print(f"\n[Error] Failed to sort assignments: {err}")
    finally:
        cursor.close()


def view_assignment_summary(connection):
    """
    Generates a summary of assignment counts grouped by subject.
    """
    query = "SELECT subject, COUNT(*) FROM assignments GROUP BY subject"
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()

        print("\n--- Assignment Summary by Subject ---")
        for row in records:
            print(f"Subject: {row[0]:<15} | Count: {row[1]}")
    except mysql.connector.Error as err:
        print(f"\n[Error] Failed to generate summary: {err}")
    finally:
        cursor.close()


def main_menu():
    """
    Interactive CLI Menu Loop.
    """
    connection = establish_connection()
    if not connection:
        return

    while True:
        print("\n--- University Assignment Tracker ---")
        print("1. Add Assignment")
        print("2. View All Assignments")
        print("3. Mark Assignment as Completed")
        print("4. Remove Assignment")
        print("5. View Assignments Sorted by Date")
        print("6. View Assignment Summary by Subject")
        print("7. Exit")

        choice = input("Select option: ")

        if choice == "1":
            title = input("Enter Title: ")
            subject = input("Enter Subject: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            add_assignment(connection, title, subject, due_date)
        elif choice == "2":
            view_assignments(connection)
        elif choice == "3":
            assignment_id = input("Enter Assignment ID: ")
            complete_assignment(connection, assignment_id)
        elif choice == "4":
            assignment_id = input("Enter Assignment ID: ")
            remove_assignment(connection, assignment_id)
        elif choice == "5":
            view_assignments_sorted(connection)
        elif choice == "6":
            view_assignment_summary(connection)
        elif choice == "7":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please select again.")

    connection.close()


if __name__ == "__main__":
    main_menu()
