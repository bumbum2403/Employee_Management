# main.py

# Import all the functions we will need from our logic modules
from src.logic import employee_manager, project_manager, performance_reviewer, reports
import datetime

def print_menu():
    """Prints the main menu of the application."""
    print("\n===== Employee Performance Tracker =====")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Add New Project")
    print("4. Assign Employee to Project")
    print("5. Submit Performance Review")
    print("6. View Projects for an Employee")
    print("7. View Performance Reviews for an Employee")
    print("8. Generate Employee-Project Report")
    print("9. Generate Employee Performance Summary")
    print("0. Exit")
    print("========================================")

def main():
    """The main function to run the CLI application."""
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add Employee
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            department = input("Enter department: ")
            hire_date = datetime.date.today().isoformat()
            employee_manager.add_employee(first_name, last_name, email, hire_date, department)

        elif choice == '2':
            # View All Employees
            employees = employee_manager.list_all_employees()
            print("\n--- All Employees ---")
            for emp in employees:
                print(f"ID: {emp['employee_id']}, Name: {emp['first_name']} {emp['last_name']}, Email: {emp['email']}")
            print("---------------------")

        elif choice == '3':
            # Add Project
            project_name = input("Enter project name: ")
            start_date = datetime.date.today().isoformat()
            project_manager.add_project(project_name, start_date)

        elif choice == '4':
            # Assign Employee to Project
            try:
                emp_id = int(input("Enter employee ID: "))
                proj_id = int(input("Enter project ID: "))
                role = input("Enter role for this project: ")
                project_manager.assign_employee_to_project(emp_id, proj_id, role)
            except ValueError:
                print("Error: Please enter valid numerical IDs.")

        elif choice == '5':
            # Submit Performance Review
            try:
                emp_id = int(input("Enter employee ID for the review: "))
                reviewer = input("Enter reviewer name: ")
                rating = float(input("Enter overall rating (1.0 - 5.0): "))
                comments = input("Enter general comments: ")
                strengths = input("Enter key strengths (optional): ")
                review_date = datetime.date.today().isoformat()
                performance_reviewer.submit_performance_review(emp_id, review_date, reviewer, rating, comments, strengths)
            except ValueError:
                print("Error: Please enter a valid number for ID and rating.")

        elif choice == '6':
            # View Projects for an Employee
            try:
                emp_id = int(input("Enter employee ID to see their projects: "))
                projects = project_manager.get_projects_for_employee(emp_id)
                print(f"\n--- Projects for Employee ID: {emp_id} ---")
                if projects:
                    for proj in projects:
                        print(f"Project: {proj['project_name']}, Role: {proj['role']}")
                else:
                    print("No projects found for this employee.")
                print("---------------------------------")
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

        elif choice == '7':
            # View Performance Reviews for an Employee
            try:
                emp_id = int(input("Enter employee ID to see their reviews: "))
                reviews = performance_reviewer.get_performance_reviews_for_employee(emp_id)
                print(f"\n--- Reviews for Employee ID: {emp_id} ---")
                if reviews:
                    for rev in reviews:
                        print(f"Date: {rev['review_date']}, Reviewer: {rev['reviewer_name']}, Rating: {rev['overall_rating']}")
                        print(f"   Comments: {rev['comments']}")
                else:
                    print("No reviews found for this employee.")
                print("---------------------------------")
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

        elif choice == '8':
            # Generate Employee-Project Report
            reports.generate_employee_project_report()

        elif choice == '9':
            # Generate Employee Performance Summary
            try:
                emp_id = int(input("Enter employee ID for performance summary: "))
                reports.generate_employee_performance_summary(emp_id)
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

        elif choice == '0':
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()