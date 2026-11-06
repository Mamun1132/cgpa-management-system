# CGPA Management System

A Flask web app for keeping students' semester results. For each student it stores the name and the CGPA and credits for 8 semesters, and shows each student's total credits and overall (credit-weighted) CGPA.

## Features

- **Add Student:** enter a name and the CGPA and credits for semesters 1–8
- **Update Student:** change a student's name and results by student ID
- **Delete Student:** remove a student by ID
- **View Students:** a table of every student with all semester results, total credits and average CGPA

## Tech stack

Python, Flask, Flask-MySQLdb, MySQL, Jinja2 templates, HTML, CSS

## Run it locally

1. Install the packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Create the database and table:
   ```bash
   mysql -u root -p < schema.sql
   ```
3. Start the app:
   ```bash
   python app.py
   ```
4. Open http://127.0.0.1:5000

Database settings default to `localhost`, user `root`, an empty password and database `cgpa_management`. Override them with the environment variables `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DB` and `SECRET_KEY`.

## Project structure

```
app.py              Flask routes: add, update, delete and view students
schema.sql          MySQL table, with total credits and average CGPA calculated by MySQL
templates/          Jinja2 pages (base, add, update, delete, view)
static/             CSS for each page
requirements.txt    Python packages
```

## Author

Md. Abdulla Al Mamun, Daffodil International University
