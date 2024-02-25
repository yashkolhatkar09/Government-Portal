# Government-Portal

Problem statement : Citizen Reporting and Monitoring System: Design a web-based platform for 
citizens to report issues, submit feedback, and monitor the progress of 
infrastructure projects, public services, and government initiatives, promoting 
transparency and accountability in governance.

![Screenshot (18)](https://github.com/yashkolhatkar09/Government-Portal/assets/138909671/840e7f2a-13bb-419b-a8ec-e675acb801de)

![image](https://github.com/ShantanuPanse/HackForge-WebCrafters-1b/assets/138909671/44f7e2d7-8af2-4bfa-bcf6-26b87fe9328a)

![image](https://github.com/ShantanuPanse/HackForge-WebCrafters-1b/assets/138909671/db3bfc4b-c1d0-4c11-a3f7-faae60dc2589)


![image](https://github.com/ShantanuPanse/HackForge-WebCrafters-1b/assets/138909671/c5437507-5369-449c-9083-492593424351)

![image](https://github.com/ShantanuPanse/HackForge-WebCrafters-1b/assets/138909671/6151ab15-a31c-490b-85a5-5471f6a5d271)

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
