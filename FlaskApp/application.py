import time
from os import system, path
from datetime import datetime
from base64 import b64encode, b64decode, b16encode, b16decode
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listens_for
from flask import Flask, render_template, redirect, request, flash, Markup, session, jsonify, url_for

application = app = Flask(__name__)

'''
##################################################################################################
###################################### Application Routes ########################################
##################################################################################################
'''
@application.route("/")
def index():
    return redirect("/home")

@application.route("/home")
def home():
    return render_template("home.html")

@application.route("/getMessage", methods=['POST'])
def getMessage():
    name = request.json['name']
    email = request.json['email']
    message = request.json['message']

    #TODO: Add message to database now!

    return jsonify("success")

###################################
# Main function where app is run. #
###################################
if __name__ == "__main__":
    public = "0.0.0.0"
    local = "127.0.0.1"
    # app.secret_key = "something"
    
    application.run(debug=True, host=public)

