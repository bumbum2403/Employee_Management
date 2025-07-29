# src/database/setup_sql.py
import sqlite3
import os

# Define the path for the database in the root of the project
DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..', '..', 'company.db')

def create_database():
    """Creates the SQLite database and the necessary tables."""

    print(f"Connecting to database at: {DB_FILEPATH}")
    # conn will be the connection to the database
    # The connect function creates the DB file if it doesn't exist
    conn = sqlite3.connect(DB_FILEPATH)

    # A cursor is used to execute SQL commands
    cursor = conn.cursor()

    # --- Create Employees Table ---
    # Stores core, structured information about each employee.
    print("Creating Employees table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        employee_id INTEGER PRIMARY KEY,      -- Unique ID for each employee. INTEGER PRIMARY KEY is auto-incrementing.
        first_name TEXT NOT NULL,             -- Employee's first name, cannot be empty.
        last_name TEXT NOT NULL,              -- Employee's last name, cannot be empty.
        email TEXT NOT NULL UNIQUE,           -- Employee's email, must be unique.
        hire_date TEXT NOT NULL,              -- Using TEXT for dates ('YYYY-MM-DD') is simple and effective in SQLite.
        department TEXT NOT NULL              -- Department name.
    );
    ''')

    # --- Create Projects Table ---
    # Stores information about each project.
    print("Creating Projects table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Projects (
        project_id INTEGER PRIMARY KEY,       -- Unique ID for each project.
        project_name TEXT NOT NULL UNIQUE,    -- Project name, must be unique.
        start_date TEXT NOT NULL,             -- Project start date.
        end_date TEXT,                        -- End date can be NULL if the project is ongoing.
        status TEXT NOT NULL                  -- e.g., 'Active', 'Completed', 'On Hold'.
    );
    ''')

    # --- Create Employee_Projects Junction Table ---
    # This table links Employees to Projects, creating a many-to-many relationship.
    # An employee can be on multiple projects, and a project can have multiple employees.
    print("Creating Employee_Projects junction table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee_Projects (
        assignment_id INTEGER PRIMARY KEY,
        employee_id INTEGER NOT NULL,
        project_id INTEGER NOT NULL,
        role TEXT NOT NULL,                   -- e.g., 'Developer', 'Project Manager'.
        FOREIGN KEY (employee_id) REFERENCES Employees (employee_id),
        FOREIGN KEY (project_id) REFERENCES Projects (project_id)
    );
    ''')

    # Commit the changes (save them to the file)
    conn.commit()

    # Close the connection
    conn.close()

    print("Database and tables created successfully.")

if __name__ == '__main__':
    create_database()