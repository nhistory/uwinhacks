"""Routes to the user auth page"""
from flask import Blueprint, render_template, request
import json

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        return render_template('login.html')
    elif(request.method == 'POST'): #login and go to home page
        email = request.form['email']
        password = request.form['password']

        with open('./website/users.json', 'r') as json_file: #storing users in a json file for now, very bad practice but fine for proof of concept
            users = json.load(json_file)
            for user in users:
                if user['email'] == email and user['password'] == password:
                    return render_template('home.html')
                    
            users.append({'email': email, 'password': password})
            with open('./website/users.json', 'w') as outfile: #if not found, add user to json file
                json.dump(users, outfile)

        return render_template('index.html')
