# src/logic/reports.py
from src.database.db_connections import get_sql_connection
from src.logic.employee_manager import get_employee_by_id
from src.logic.performance_reviewer import get_performance_reviews_for_employee

def generate_employee_project_report():
    """
    Generates a formatted report of which employees are on which projects.
    This function demonstrates a complex JOIN across three tables.
    """
    print("\n--- Employee-Project Assignment Report ---")
    conn = get_sql_connection()
    cursor = conn.cursor()

    sql = """
    SELECT 
        e.first_name, 
        e.last_name, 
        p.project_name, 
        ep.role
    FROM Employees e
    JOIN Employee_Projects ep ON e.employee_id = ep.employee_id
    JOIN Projects p ON ep.project_id = p.project_id
    ORDER BY e.last_name, p.project_name;
    """

    cursor.execute(sql)
    report_data = cursor.fetchall()
    conn.close()

    if not report_data:
        print("No project assignments found.")
        return

    # Print table headers with padding for alignment
    print(f"{'Employee Name':<25} | {'Project Name':<30} | {'Role':<20}")
    print("-" * 80)

    # Print each row of the report
    for row in report_data:
        employee_name = f"{row['first_name']} {row['last_name']}"
        print(f"{employee_name:<25} | {row['project_name']:<30} | {row['role']:<20}")

    print("-" * 80)


def generate_employee_performance_summary(employee_id):
    """
    Generates a summary of an employee's performance.
    This function shows how to combine data from SQL and NoSQL.
    """
    print(f"\n--- Performance Summary for Employee ID: {employee_id} ---")

    # 1. Get employee details from SQL
    employee = get_employee_by_id(employee_id)
    if not employee:
        print("Error: Employee not found.")
        return

    print(f"Employee: {employee['first_name']} {employee['last_name']}")
    print(f"Department: {employee['department']}")
    print("-" * 50)

    # 2. Get performance reviews from NoSQL (MongoDB)
    reviews = get_performance_reviews_for_employee(employee_id)
    if not reviews:
        print("No performance reviews found for this employee.")
        return

    # 3. Process the combined data
    total_rating = 0
    all_strengths = []

    for review in reviews:
        total_rating += review.get('overall_rating', 0)
        if 'strengths' in review:
            all_strengths.append(review['strengths'])

    average_rating = total_rating / len(reviews) if reviews else 0

    print(f"Number of Reviews: {len(reviews)}")
    print(f"Average Overall Rating: {average_rating:.2f} / 5.00")

    if all_strengths:
        print("\nKey Strengths Mentioned:")
        for strength in all_strengths:
            print(f"- {strength}")

    print("-" * 50)



    """
    What this file does: It provides high-level reporting functions.
    Notice how generate_employee_performance_summary calls functions
    from both employee_manager (SQL) and performance_reviewer (NoSQL) to create a unified report. 
    Like the other logic modules, you do not run this file directly.


    This file is designed to be imported by other modules or scripts that need to generate reports.
    """