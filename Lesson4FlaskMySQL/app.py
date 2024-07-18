from flask import Flask, jsonify, request
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# create a connection to the database
db = mysql.connector.connect(
   host=os.getenv("DB_HOST"),
   user=os.getenv("DB_USER"),
   password=os.getenv("DB_PASSWORD"),
   database=os.getenv("DB_NAME")
)


# print(db)
# creation of the cursor variable which will be used to interact with the database
cursor = db.cursor(dictionary=True)
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

def add_airline(airline_name, country_id):
    cursor.execute("insert into airlines (name, country_id) VALUES (%s, %s)", (airline_name, country_id))
    db.commit()
    return "Airline added successfully"


def update_airline(airline):
    cursor.execute("UPDATE airlines SET Name = %s, country_id = %s WHERE id = %s",
                   (airline['name'], airline['country_id'], airline['id']))
    db.commit()
    if cursor.rowcount > 0:
        return f"Successfully updated {cursor.rowcount}"
    else:
        return "no rows updated"




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

@app.route('/api/addAirline', methods=['POST'])
def add_airline_api():
    data = request.json
    airline_name = data['Name']
    country_id = data['Country_Id']
    result = add_airline(airline_name, country_id)
    return jsonify(result)


@app.route('/api/updateAirline', methods=['PUT'])
def update_airline_api():
    airline = request.json
    result = update_airline(airline)
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True, port=5005)





# Steps to run the app:
# 1 -> install python -> https://www.python.org/downloads/
# 2 -> create .venv -> python -m venv .venv
# 3 -> install flask -> pip install flask
#           instead install requirements.txt -> pip install -r requirements.txt
# 4 -> run the app -> python app.py (flask run)