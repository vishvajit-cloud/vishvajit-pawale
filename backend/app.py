from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    course = request.form['course']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email, age, course) VALUES (%s, %s, %s, %s)",
        (name, email, age, course)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return "Student Registered Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME")
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    course = request.form['course']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email, age, course) VALUES (%s, %s, %s, %s)",
        (name, email, age, course)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return "Student Registered Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

