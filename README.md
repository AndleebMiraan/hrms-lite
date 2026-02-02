# HRMS Lite

## Project Overview
HRMS Lite is a lightweight Human Resource Management System designed to allow an admin to manage employee records and track daily attendance. The application provides a clean, professional interface and includes functionalities to add, view, and delete employees as well as mark and view attendance records.

### Features
- Employee Management
  - Add new employee with ID, Name, Email, and Department
  - View list of employees
  - Delete employee
- Attendance Management
  - Mark attendance (Present/Absent) for each employee by date
  - View attendance records per employee
- Dashboard
  - Total employees
  - Present today
  - Absent today
- AJAX-based forms for smooth user experience
- Responsive UI using Bootstrap
- Basic validation and error handling

## Tech Stack
- **Frontend:** HTML, CSS (Bootstrap, Choices.js, Flatpickr), JavaScript, jQuery
- **Backend:** Python, Django
- **Database:** SQLite (default Django DB)
- **Deployment:** Render (Backend + Frontend)

## Steps to Run the Project Locally
1. **Clone the repository**
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd hrms
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
Open your browser and navigate to `http://127.0.0.1:8000/`

## Assumptions or Limitations
- Single admin user; no authentication implemented for simplicity.
- Attendance is only tracked by Present/Absent status.
- Employee deletion is permanent; no soft delete.
- No advanced HR features like payroll, leave management, or roles.
- The frontend is tightly coupled with the backend Django templates (no SPA).
- Database is SQLite by default; production deployment may use PostgreSQL/MySQL.

## Live Application URL
[HRMS Lite on Render](https://hrms-lite-r31l.onrender.com/)

## GitHub Repository
[HRMS Lite Source Code]([<YOUR_GITHUB_REPO_URL>](https://github.com/AndleebMiraan/hrms-lite.git))

