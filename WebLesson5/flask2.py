from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "hello world"
listfromdb =  ["Monday", "Tuesday", "Wednesday",  "Saturday", "Sunday"]

@app.route('/generic_welcome')
def generic_welcome():
    return render_template("index.html" , first_name ="Arja",  age=15)



@app.route('/days/')
@app.route('/days/<int:selected_day>')
def days(selected_day=None):
    return render_template("daysOfWeek.html", days = listfromdb, selected_day = selected_day)


@app.route('/addDay', methods = ['POST'])
def addDay():
    newDay = request.form['newDay']
    if newDay not in listfromdb:
        listfromdb.append(newDay)
        # db. save 
        return render_template("daysOfWeek.html", days = listfromdb)
    else:
         return render_template("daysOfWeek.html", days = listfromdb, error = "Day already exists")
        
    
@app.route('/user/')    
@app.route('/user/<username>')
def user(username="default"):
    return "Hello, " + username


@app.route('/uploadFile')
def uploadFile():
    return render_template("uploadFile.html")

UPLOAD_FOLDER = 'static/images'
@app.route('/upload', methods = ['POST'])
def upload():
    f = request.files['photo']
    file_path = UPLOAD_FOLDER + '/' + '1.jpg' # static/images/filename
    f.save(file_path)
    return "File uploaded successfully"




# create route '/days/' to present days of the week based on the list paramerter
# each day should be a link to #
#  link in html is "<a href = "#"> text </a>"


if __name__ == '__main__':
    app.run(debug=True, port=5001)