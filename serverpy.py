<<<<<<< HEAD
import csv
from flask import Flask, render_template,url_for, request, redirect


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database1.txt', mode='a') as database:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{firstname},{lastname},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer =  csv.writer(database2, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([firstname, lastname, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/index.html')
        except:
            return 'Database did not saved.'
    else:
=======
import csv
from flask import Flask, render_template,url_for, request, redirect


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database1.txt', mode='a') as database:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{firstname},{lastname},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer =  csv.writer(database2, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([firstname, lastname, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/index.html')
        except:
            return 'Database did not saved.'
    else:
>>>>>>> 9d3817ab3d481e831872e254d9ab594292a035c5
        return 'something wrong...Try Again!!!!'