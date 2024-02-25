# Government-Portal

Problem statement : Citizen Reporting and Monitoring System: Design a web-based platform for 
citizens to report issues, submit feedback, and monitor the progress of 
infrastructure projects, public services, and government initiatives, promoting 
transparency and accountability in governance.

![Screenshot (15)](https://github.com/yashkolhatkar09/Government-Portal/assets/138909671/a862e2f7-edc2-4fe6-801a-04c869ee9b42)


![Screenshot (12)](https://github.com/yashkolhatkar09/Government-Portal/assets/138909671/f23317f9-fa39-4cc7-816f-a1faa36a0a73)


![Screenshot (13)](https://github.com/yashkolhatkar09/Government-Portal/assets/138909671/afcf78d5-d1bb-4cd9-9e79-cae9d09687b7)

![Screenshot (14)](https://github.com/yashkolhatkar09/Government-Portal/assets/138909671/382f7971-b791-4c2d-841e-549d0d52dc70)



# Government Portal

This repository contains the code for a Government Portal, including different views for Operators and Citizens. The project is developed using HTML, CSS, and Python with Flask.

## Operator View

### Login Page
- File: operator_login.html
- Path: /operator_login

The login page for the operator includes a password input form to access the operator dashboard.

### Operator Dashboard
- File: operator_dashboard.html
- Path: /operator_dashboard

The operator dashboard allows the government official to submit reports about various events.

## User View

### User Login Page
- File: user_login.html
- Path: /user_login

The user login page allows citizens to log in and submit reports about issues they encounter.

### User Dashboard
- File: user_dashboard.html
- Path: /user_dashboard

The user dashboard provides a form for citizens to submit issue reports, select categories, and provide additional details.

## Backend

The backend of the project is developed using Flask, a Python web framework.

### Flask App
- File: app.py

The Flask application handles routing, form submissions, and interactions with the MySQL database.

## Database

The project uses a MySQL database to store information about events and user reports.

### Database Schema
- Table: event
  - Fields: id, title, startDate, category, progress, description

- Table: users
  - Fields: id, description, category

## Running the Application

To run the application, make sure you have Flask installed. Use the following commands:
 - pip install flask
 - pip install mysql-connector
  

```bash
