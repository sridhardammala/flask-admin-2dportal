import os
import json
# from flask import Flask, request, jsonify
from google.cloud import storage
from dotenv import load_dotenv 
from flask import Flask, flash, render_template, session, redirect, url_for, session, request, g, jsonify


app = Flask(__name__)

load_dotenv()

@app.route("/hello")
def hello_world():
    return "Hello, World!"

# @app.before_request
# def before_request():
#     if 'uname' in session:
#         g.uname = session['uname']
#     else:
#         g.uname = None

@app.route('/',methods=['GET','POST'])
def index():
    # session.pop('uname', None)
    if request.method == 'POST':
        print(request.form)
        uname = request.form['uname']
        pword = request.form['pword']
        if uname == "test" and "pword" == "test":
            return redirect(url_for("opspage"))
        else:
            flash("Login ERROR: Either the user name or password is incorrect")   
    return render_template('index.html')
    
@app.route('/opspage')
def opspage():
    session.pop('_flashes', None)
    if not g.uname:
        flash("You have not logged in. Please login to proceed")
        return render_template('index.html')

    return render_template('opspage.html')


@app.route('/download_file_from_gcs', methods=['POST'])
def download_file_from_gcs():
    print(" I am in download_file_from_gcs")
    try:
        print(" I am in download_file_from_gcs")
        json_data = request.json
        print(json_data.keys())
        if 'bucketName' not in json_data.keys() or 'fileName' not in json_data.keys():
            return jsonify({"error": "Both 'bucketName' and 'fileName' are required in the JSON data."}), 400
        print(json_data)
        bucket_name = json_data['bucketName']
        file_name = json_data['fileName']
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        # Download the file to a temporary directory within the pod
        local_temp_destination = f'/app/data/{file_name}'  # Temporary storage within the pod
        # Ensure the directory structure exists
        os.makedirs(os.path.dirname(local_temp_destination), exist_ok=True)
        print(f'Downloading the file {file_name} to {local_temp_destination}')
        blob.download_to_filename(local_temp_destination)
        # # # Move the file to the PVC mount path
        # pvc_mount_path = '/app/data'  # PVC mount path in the container
        # local_pvc_destination = os.path.join(pvc_mount_path, file_name)
        # # Ensure the directory structure exists
        # os.makedirs(os.path.dirname(local_pvc_destination), exist_ok=True)
        # os.rename(local_temp_destination, local_pvc_destination)

        return jsonify({"message": f"File '{file_name}' downloaded to PVC at '{local_temp_destination}' successfully."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run('0.0.0.0', port=5000, debug=True)



