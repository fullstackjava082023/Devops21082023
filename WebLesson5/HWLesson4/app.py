from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/anotherRoute')
def anotherRoute():
    return '<ul><li><h1>HEADER</h1></li></ul>'


@app.route('/addContact')
def addContact():
    return render_template('addContactForm.html')


@app.route('/viewContacts' , methods=['GET', 'POST'])
def viewContacts():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)