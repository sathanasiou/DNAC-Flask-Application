############################################ 
#### Example: buttons and actions ########
############################################ 

### Good link : https://plainenglish.io/blog/how-to-create-a-basic-form-in-python-flask-af966ee493fa
# templates should be under the template folder
### Templates : https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from crypt import methods
from pyexpat.errors import messages
from flask import Flask, render_template, request
from flask import jsonify, redirect, url_for
from flask import send_file, make_response

# Libraries for DNAC start: 
#from asyncore import write
from csv import writer
import site
from turtle import shape
from urllib import response
from dnacentersdk import api
import json
import os
from openpyxl import Workbook
# import pandas as pd
# import numpy as np

# Libraries for DNAC end


app = Flask(__name__)

# Simple About page -- Only text 

@app.route('/')
def about():
    return render_template('about.html')

# Get user input example:

@app.route("/input", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["interface"])
        print(request.form["ip"])
        print(request.form["subnet"])
        return 'OK' 

    return render_template("home.html")

# Parse input in excel:

@app.route("/submit-form", methods=['POST'])
def submit_form():
    # get data from the form
    interface = request.form["interface"]
    ip = request.form["ip"]
    subnet = request.form["subnet"]

    wb = Workbook()
    ws = wb.active

    ws['A1'] = "Interface"
    ws['B1'] = 'IP'
    ws['C1'] = 'Subnet'
    ws['A2'] = interface
    ws['B2'] = ip
    ws['C2'] = subnet

    ws.save('test_data.xlsx')

    return render_template("download.html")

# Download excel:

@app.route('/download')
def download_file():

    path = 'test_data.xlsx'
    response = make_response(send_file(path,as_attachment=True))
    response.headers['Content-Disposition'] = 'attachment; filename=test_data.xlsx'
    
    return response

# DNAC begin:

@app.route('/test-button')
def button():
    return render_template('button.html')

@app.route('/api/sites', methods=['GET'])
def get_sites():
    ##### Connection to DNAC ####
    dnac = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com', username='devnetuser', password='Cisco123!', verify=False)

    sites = dnac.sites.get_site()
    names= []
    for i in range(len(sites.response)):
        names.append(sites.response[i].name)
    return render_template('sites.html', response=names)

def download_sites():
    path = 'test.txt'
    return send_file(path, as_attachment=True)
 
# End DNAC

# Comments page:

@app.route('/comments/')
def comments():
    comments = ['Choose 1.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8007 )

# http://127.0.0.1:8000/comments/

# @app.route("/", methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if request.form.get('action1') == 'VALUE1':
#             pass # do something
#         elif  request.form.get('action2') == 'VALUE2':
#             pass # do something else
#         else:
#             pass # unknown
#     elif request.method == 'GET':
#         return render_template('index.html', form= form)
    
#     return render_template("index.html")