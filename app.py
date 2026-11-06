import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

# MySQL Configuration
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'cgpa_management')

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        semesters = [(request.form[f'sem{i}_cgpa'], request.form[f'sem{i}_credit']) for i in range(1, 9)]

        cursor = mysql.connection.cursor()
        query = """
        INSERT INTO students (name, sem1_cgpa, sem1_credit, sem2_cgpa, sem2_credit, 
                              sem3_cgpa, sem3_credit, sem4_cgpa, sem4_credit,
                              sem5_cgpa, sem5_credit, sem6_cgpa, sem6_credit,
                              sem7_cgpa, sem7_credit, sem8_cgpa, sem8_credit)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (name, *[val for pair in semesters for val in pair]))
        mysql.connection.commit()
        cursor.close()

        flash('Student added successfully!', 'success')
        return redirect(url_for('add_student'))

    return render_template('add_student.html')

# update the student information part

@app.route('/update_student', methods=['GET', 'POST'])
def update_student():
    if request.method == 'POST':
        # Retrieve student ID and updated values
        student_id = request.form['id']
        name = request.form['name']
        semesters = [(request.form[f'sem{i}_cgpa'], request.form[f'sem{i}_credit']) for i in range(1, 9)]

        cursor = mysql.connection.cursor()
        query = """
        UPDATE students
        SET name = %s,
            sem1_cgpa = %s, sem1_credit = %s,
            sem2_cgpa = %s, sem2_credit = %s,
            sem3_cgpa = %s, sem3_credit = %s,
            sem4_cgpa = %s, sem4_credit = %s,
            sem5_cgpa = %s, sem5_credit = %s,
            sem6_cgpa = %s, sem6_credit = %s,
            sem7_cgpa = %s, sem7_credit = %s,
            sem8_cgpa = %s, sem8_credit = %s
        WHERE id = %s;
        """
        cursor.execute(query, (name, *[val for pair in semesters for val in pair], student_id))
        mysql.connection.commit()
        cursor.close()

        flash('Student information updated successfully!', 'success')
        return redirect(url_for('update_student'))

    return render_template('update_student.html')

# update the student information part


# Delete student Route

@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        # Retrieve the student ID to delete
        student_id = request.form['id']

        # Delete the student record from the database
        cursor = mysql.connection.cursor()
        query = "DELETE FROM students WHERE id = %s;"
        cursor.execute(query, (student_id,))
        mysql.connection.commit()
        cursor.close()

        flash('Student information deleted successfully!', 'success')
        return redirect(url_for('delete_student'))

    return render_template('delete_student.html')

# Delete student Route

# View Student route

@app.route('/view_students', methods=['GET'])
def view_students():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM students;"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()

    return render_template('view_students.html', students=students)


# View Student route

if __name__ == '__main__':
    app.run(debug=True)
