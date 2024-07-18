from flask import Flask , render_template, request

# create flask application
app = Flask(__name__)


@app.route("/")
def index():
    print("got the request!!")


@app.route("/start")
def start():
    return "Hello world"

UPLOAD_FOLDER = 'static/images'

@app.route("/uploadFile" , methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        f = request.files['photo']
        file_path = UPLOAD_FOLDER + "/" + f.filename
        f.save(file_path)
        return f"File {f.filename} uploaded"
    else :
        return render_template("uploadPhoto.html")


@app.route('/html')
def html():
    return "<h1>Hello world!</h1>  <ul><li>sunday</li><li>wendesday</li> </ul>"


@app.route('/htmlFile')
def htmlFile():
    return render_template("index.html")

@app.route('/addNewContact')
def addNewContact():
    return render_template("addContactForm.html")

listfromdb = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

@app.route('/day/<int:day_number>')
def showDay(day_number):
    icons = ["&#127771;", "&#127771;", "&#128197;", "&#9729;", "&#128125;","&#9729;", "&#128125;"]
    if day_number < len(listfromdb):
        return f"<h1>{listfromdb[day_number]}</h1>{icons[day_number]}</i>"
    else:
        return "Invalid day number"
   
@app.route('/days/')     
@app.route('/days/<int:day_number>')    
def showDays(day_number=None):
    return render_template("days.html", listfromdb = listfromdb , selected_day = day_number)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

if __name__ == "__main__":
    # run flask app on port 5000
    app.run(port=5000, debug=True)