from flask import Flask, jsonify, request
import mysql.connector



# create a connection to the database
db = mysql.connector.connect(
   host="localhost",
   user="root",
   password="admin",
   database="flights_system"
)


# print(db)
# creation of the cursor variable which will be used to interact with the database
cursor = db.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS flights_system")



def get_countries():
    # select all countries from the database
    cursor.execute("SELECT * FROM countries")
    result = cursor.fetchall()
    return result


# changed to be secured from sql injection
def get_country_by_id(id):
    query = "SELECT * FROM countries WHERE id = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    return result


# print(get_country_by_id(1))


def add_country(name):
    query = f"INSERT INTO countries (name) VALUES ('{name}')"
    cursor.execute(query)
    db.commit()
    return "Country added successfully"


# add_country('Nicaragua')


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Welcome'


@app.route('/api/getCountries')
def get_countries_api():
    result = get_countries()
    return jsonify(result)


@app.route('/api/getCountryById/<id>')
def get_country_by_id_api(id):
    result = get_country_by_id(id)
    return jsonify(result)


@app.route('/api/addCountry', methods=['POST'])
def add_country_api():
    data = request.json
    name = data['name']
    result = add_country(name)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5005)





# Steps to run the app:
# 1 -> install python -> https://www.python.org/downloads/
# 2 -> create .venv -> python -m venv .venv
# 3 -> install flask -> pip install flask
#           instead install requirements.txt -> pip install -r requirements.txt
# 4 -> run the app -> python app.py (flask run)