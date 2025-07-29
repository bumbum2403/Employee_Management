
# Employee Performance Tracking System


A simple command-line interface (CLI) application designed to manage employee data, project assignments, and performance reviews. This system utilizes a hybrid database approach, leveraging SQLite for structured relational data and MongoDB for flexible, semi-structured review data.



## Features

- Employee Management: Add, view, and manage employee records.

- Project Management: Create new projects and assign employees with specific roles.

- Performance Tracking: Submit detailed performance reviews for employees.

- Hybrid Database Interaction: Stores employee/project data in a local SQLite database and performance reviews in a cloud-hosted MongoDB Atlas cluster.

- Reporting: Generate consolidated reports on employee-project assignments and individual performance summaries.

- Secure Configuration: Uses a .env file to securely manage database credentials.


## Tech Stack


**Python 3:** Core application logic.

**SQLite:** Relational database for structured data (employees, projects).

**MongoDB:** NoSQL document database for semi-structured data (performance reviews).

**pymongo:** Python driver for MongoDB.

**python-dotenv:** For managing environment variables.




## Setup and Installation

Follow these steps to get the application running on your local machine.

1. Clone the Repository


```bash
git clone <your-repository-url>
cd employee_performance_tracker
```

2. Create and Activate a Virtual Environment

- On MacOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```
- On Windows:

```bash
python3 -m venv venv
.\venv\Scripts\activate
```

3. Create the .env File

This file stores your MongoDB connection string securely.

Create a file named .env in the root directory of the project.

Add your MongoDB Atlas connection string to it like so:

```bash
MONGO_URI="mongodb+srv://<username>:<password>@yourcluster.mongodb.net/?retryWrites=true&w=majority"
``` 

**Note:** The `.gitignore` file is configured to prevent the .env file from being committed.

4. Install Dependencies

Install all the necessary Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

5. Run the Application 

```bash
python main.py
``` 




## Future Improvements


- Web Interface: Develop a web-based front end using a framework like Flask or FastAPI.

- Advanced Reporting: Implement more complex analytics, such as department-level performance metrics or project completion rates.

- User Authentication: Add user roles (e.g., HR, Manager, Employee) with different permissions.

- Unit Testing: Develop a suite of unit and integration tests using pytest to ensure code reliability.

- Containerization: Package the application with Docker for easier deployment and environment consistency.


