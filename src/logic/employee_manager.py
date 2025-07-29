# src/logic/employee_manager.py
import sqlite3
from src.database.db_connections import get_sql_connection

def add_employee(first_name, last_name, email, hire_date, department):
    """Adds a new employee to the Employees table."""
    conn = get_sql_connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO Employees (first_name, last_name, email, hire_date, department) VALUES (?, ?, ?, ?, ?)"
        # Using placeholders (?) is crucial to prevent SQL injection attacks.
        cursor.execute(sql, (first_name, last_name, email, hire_date, department))
        conn.commit()
        print(f"Employee '{first_name} {last_name}' added successfully.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        # This error occurs if the email (UNIQUE column) already exists.
        print(f"Error: An employee with the email '{email}' already exists.")
        return None
    finally:
        conn.close()

def get_employee_by_id(employee_id):
    """Retrieves an employee's details by their ID."""
    conn = get_sql_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Employees WHERE employee_id = ?"
    cursor.execute(sql, (employee_id,))
    employee = cursor.fetchone() # Fetches the first matching row
    conn.close()
    return dict(employee) if employee else None

def list_all_employees():
    """Retrieves a list of all employees."""
    conn = get_sql_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Employees"
    cursor.execute(sql)
    employees = cursor.fetchall() # Fetches all matching rows
    conn.close()
    # Convert list of Row objects to list of dictionaries
    return [dict(employee) for employee in employees]