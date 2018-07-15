import dbFunctions as df
from firebase import firebase
from flask import Flask, render_template, redirect, request, flash, jsonify, make_response

application = app = Flask(__name__)

dbUtils = df.Functions()

'''
##################################################################################################
###################################### Application Routes ########################################
##################################################################################################
'''
@application.route("/")
def index():
    return make_response(redirect("/home"), 302)

@application.route("/home")
def home():
    return make_response(render_template("home.html"), 200)

@application.route("/sendMessage", methods=['POST'])
def sendMessage():
    name = request.json['name']
    email = request.json['email']
    message = request.json['message']

    if dbUtils.addMessage(name, email, message):
        status = "Yay! Message has successfully been sent!"
        code = 200
    else:
        status = "Oh no, something's wrong! Your message didn't send!"
        code = 500
    
    return make_response(jsonify(message=status), code)

###################################
# Main function where app is run. #
###################################
if __name__ == "__main__":
    public = "0.0.0.0"
    local = "127.0.0.1"
    app.secret_key = "something"
    
    application.run(debug=False, host=public)

