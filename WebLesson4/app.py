from flask import Flask , render_template

# create flask application
app = Flask(__name__)


@app.route("/")
def index():
    print("got the request!!")


@app.route("/start")
def start():
    return "Hello world"



@app.route('/html')
def html():
    return "<h1>Hello world!</h1>  <ul><li>sunday</li><li>wendesday</li> </ul>"


@app.route('/htmlFile')
def htmlFile():
    return render_template("index.html")




if __name__ == "__main__":
    # run flask app on port 5000
    app.run(port=5000, debug=True)