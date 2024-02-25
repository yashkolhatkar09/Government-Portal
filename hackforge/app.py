from flask import Flask, render_template, request
import mysql.connector
from datetime import date

app = Flask(__name__, static_folder="static")

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9145036362",
    database="hackforge"
    
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitoppassword', methods=['POST'])
def validate():
    password = request.form['oppassword']
    if password == 'useradmin':
        cursor.execute("SELECT * FROM event")
        events = cursor.fetchall()
        return render_template('operator.html', events=events)
    return "Error"

@app.route('/userlogin', methods=['POST'])
def validateuser():
    cursor.execute("SELECT * FROM event")
    events = cursor.fetchall()
    return render_template("user.html", events=events)

@app.route('/submit', methods=['POST'])
def submit_event():
    event_title = request.form['event-title']
    Category = request.form['Category']
    event_description = request.form['event-description']
    startDate = date.today()
    progress = '0'

    if '@' in event_title:  # Corrected condition
        return render_template('operator.html')

    # Insert data into the database using parameterized query
    sql = "INSERT INTO event (title, startDate, category, progress, description) VALUES (%s, %s, %s, %s, %s)"
    val = (event_title, startDate, Category, progress, event_description)
    cursor.execute(sql, val)
    db.commit()

    cursor.execute("SELECT * FROM event")
    events = cursor.fetchall()
    return render_template('operator.html', events=events)
    
@app.route('/submitreport', methods=['POST'])
def submit_report():
    userid = request.form['userid']
    description = request.form['description']
    category = request.form['category']
    # location = request.form['location']

    # Insert data into the database using parameterized query
    sql = "INSERT INTO users (id, description, category) VALUES (%s, %s, %s)"
    val = (userid, description, category)
    cursor.execute(sql, val)
    db.commit()

    cursor.execute("SELECT * FROM event")
    events = cursor.fetchall()
    return render_template('user.html', events=events)

# @app.route('/submitreport',methods=['POST'])
# def submit_report():
#     userid = 

if __name__ == '__main__':
    app.run(debug=True)
