# src/logic/project_manager.py
import sqlite3
from src.database.db_connections import get_sql_connection

def add_project(project_name, start_date, end_date=None, status='Planning'):
    """Adds a new project to the Projects table."""
    conn = get_sql_connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO Projects (project_name, start_date, end_date, status) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (project_name, start_date, end_date, status))
        conn.commit()
        print(f"Project '{project_name}' added successfully.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Error: A project with the name '{project_name}' already exists.")
        return None
    finally:
        conn.close()

def assign_employee_to_project(employee_id, project_id, role):
    """Assigns an employee to a project in the Employee_Projects table."""
    conn = get_sql_connection()
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO Employee_Projects (employee_id, project_id, role) VALUES (?, ?, ?)"
        cursor.execute(sql, (employee_id, project_id, role))
        conn.commit()
        print(f"Successfully assigned employee {employee_id} to project {project_id} as '{role}'.")
        return cursor.lastrowid
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()

def get_projects_for_employee(employee_id):
    """Retrieves all projects an employee is assigned to."""
    conn = get_sql_connection()
    cursor = conn.cursor()
    # A JOIN query combines rows from multiple tables based on a related column.
    sql = """
    SELECT p.project_id, p.project_name, p.status, ep.role
    FROM Projects p
    JOIN Employee_Projects ep ON p.project_id = ep.project_id
    WHERE ep.employee_id = ?
    """
    cursor.execute(sql, (employee_id,))
    projects = cursor.fetchall()
    conn.close()
    return [dict(project) for project in projects]