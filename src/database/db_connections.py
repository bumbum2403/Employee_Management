# src/database/db_connections.py
import sqlite3
import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

# --- SQL (SQLite) Connection ---

# Define the path for the database in the root of the project
DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..', '..', 'company.db')

def get_sql_connection():
    """
    Establishes a connection to the SQLite database.
    Also ensures that the necessary tables are created.
    Returns a connection object.
    """
    conn = sqlite3.connect(DB_FILEPATH)
    # Use row_factory to get results as dictionaries instead of tuples
    conn.row_factory = sqlite3.Row 

    cursor = conn.cursor()

    # The CREATE TABLE IF NOT EXISTS command prevents errors on subsequent runs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        hire_date TEXT NOT NULL,
        department TEXT NOT NULL
    );''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Projects (
        project_id INTEGER PRIMARY KEY,
        project_name TEXT NOT NULL UNIQUE,
        start_date TEXT NOT NULL,
        end_date TEXT,
        status TEXT NOT NULL
    );''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee_Projects (
        assignment_id INTEGER PRIMARY KEY,
        employee_id INTEGER NOT NULL,
        project_id INTEGER NOT NULL,
        role TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES Employees (employee_id),
        FOREIGN KEY (project_id) REFERENCES Projects (project_id)
    );''')

    conn.commit()
    return conn

# --- NoSQL (MongoDB) Connection ---

# !! IMPORTANT !!
# Replace this with your actual MongoDB Atlas connection string.
# For better security, use environment variables in a real application.
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "performance_reviews_db"
COLLECTION_NAME = "reviews"

def get_mongo_collection():
    """
    Establishes a connection to MongoDB and returns the 'reviews' collection object.
    """
    try:
        client = MongoClient(MONGO_URI)
        # The ping will confirm a successful connection
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        return collection
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None