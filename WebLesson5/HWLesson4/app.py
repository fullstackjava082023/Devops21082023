from flask import Flask, render_template,redirect,request
import mysql.connector

app = Flask(__name__)


# Create a global connection object
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

def execute_query(query, values):
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/anotherRoute')
def anotherRoute():
    return '<ul><li><h1>HEADER</h1></li></ul>'


@app.route('/addContact', methods=['GET', 'POST'])
def addContact():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Save the contact to the database
        query = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
        values = (name, email, phone)
        execute_query(query, values)
        
        return redirect('/viewContacts')
    else:
        return render_template('addContactForm.html')

# Close the connection when the application is shut down
@app.teardown_appcontext
def close_connection(exception):
    connection.close()


@app.route('/viewContacts' , methods=['GET', 'POST'])
def viewContacts():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)