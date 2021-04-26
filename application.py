
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import os
from comprehend_helper import process_csv_file
from collections import Counter
import operator

application = Flask(__name__)
application.config.from_pyfile('config.py')

# initialize an empty output dict at the global scope
data_output = {}

### Renders upload screen
@application.route("/")
def upload():
    return render_template("upload.html")

### Save file and redirect to dashboard UI
@application.route("/saveFile", methods=['POST'])
def saveFile():
    f = request.files['filename']
    application.config['UPLOAD_FILE_PATH'] = os.path.join(application.config['UPLOAD_FOLDER'], f.filename)
    f.save(application.config['UPLOAD_FILE_PATH'])

    # reset output data when a new file is uploaded
    global data_output
    data_output = {}

    return redirect("/dashboard", code=302)

### API output
@application.route("/data")
def data():

    # if a file hasn't been uploaded yet, redirect to upload page
    if 'UPLOAD_FILE_PATH' not in application.config:
        return redirect("/")

    # check if we need to process the input file
    global data_output
    if not data_output:
        data_output = process_csv_file(application.config['UPLOAD_FILE_PATH'], max_rows=200)

    return jsonify(data_output)


### Render dashboard UI
@application.route("/dashboard")
def dashboard():
    
    return render_template("dashboard.html")

if __name__ == '__main__':
    application.run()