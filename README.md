# Kaam365 – Local Service Management Platform

## Project Overview
Kaam365 is a Django-based Local Service Management Platform developed to connect customers with skilled local service providers such as plumbers, electricians, carpenters, painters, and helpers.

The platform enables users to book services, manage projects, track schedules, and monitor payment status through a secure role-based authentication system.

---

## Tech Stack
- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap

---

## Key Features

### Role-Based Authentication
- Admin
- Customer
- Worker
- Secure login and logout functionality

### Service Management
- Add and manage worker categories
- Assign workers to service projects
- View service history

### Project and Schedule Tracking
- Create and manage service projects
- Assign start and completion dates
- Track active and completed projects

### Payment Management
- Track payment status (Pending / Completed)
- Maintain structured payment records

### Admin Dashboard
- Monitor users and services
- Manage workers and categories
- View project statistics

---

## Database Design
- Structured models implemented using Django ORM
- Relationships between Users, Roles, Projects, and Payments
- SQLite database used for development

---
## Installation

Clone the repository:

git clone https://github.com/tanushreenamdeo/Kaam365-Django.git  
cd Kaam365-Django  

Create a virtual environment and install dependencies:

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  

Run the server:

python manage.py migrate  
python manage.py runserver  
## Installation and Setup
