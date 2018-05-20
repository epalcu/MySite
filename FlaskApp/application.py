# import dbTables as dt
# import dbFunctions as df
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, request, flash, Markup, session, jsonify, url_for

application = app = Flask(__name__)
# application.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"
# application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# application.config['SQLALCHEMY_ECHO'] = False
# dt.db.app = application
# dt.db.init_app(application)

# dt.db.create_all()

# dbUtils = df.Functions(dt.db)

'''
##################################################################################################
###################################### Application Routes ########################################
##################################################################################################
'''
@application.route("/")
def index():
    return redirect("/home"), 302

@application.route("/home")
def home():
    return render_template("home.html"), 200

@application.route("/getMessage", methods=['POST'])
def getMessage():
    name = request.json['name']
    email = request.json['email']
    message = request.json['message']

    dbUtils.addMessage(name, email, message)

    return jsonify("success"), 200

###################################
# Main function where app is run. #
###################################
if __name__ == "__main__":
    public = "0.0.0.0"
    local = "127.0.0.1"
    # app.secret_key = "something"
    
    application.run(debug=True, host=public)

