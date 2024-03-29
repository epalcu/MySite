import json
import boto3
from flask_mail import Mail, Message
from flask import Flask, render_template, redirect, request, flash, jsonify, make_response


'''
##################################################################################################
#################################### Begin Application Globals ###################################
##################################################################################################
{'''


app = Flask(__name__)


'''}
##################################################################################################
##################################### End Application Globals ####################################
##################################################################################################
'''


'''
##################################################################################################
##################################### Begin Application Pages ####################################
##################################################################################################
{'''


@app.route("/")
def index():
    return make_response(redirect("/home"), 302)


@app.route("/home")
def home():
    return make_response(render_template("home.html"), 200)


'''}
##################################################################################################
###################################### End Application Pages #####################################
##################################################################################################
'''


'''
##################################################################################################
##################################### Begin Application Routes ###################################
##################################################################################################
{'''

def configureMailClient():
    print app
    client = boto3.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )

    creds = json.loads(client.get_secret_value(
        SecretId='elliasWebsiteEmailCreds'
    )['SecretString'])

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = creds['username']
    app.config['MAIL_PASSWORD'] = creds['password']
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    return Mail(app)


@app.route('/contact/message', methods=['POST'])
def contactMessage():
    name = request.json['name']
    email = request.json['email']
    message = request.json['message']

    # Configure our mail client
    mail = configureMailClient()

    # E-mail the user
    msg = Message(
        "Yo! Website message!",
        sender="elliaspalcu@gmail.com",
        recipients=["elliaspalcu@gmail.com"]
    )

    msg.body = "From: {0}\n\nE-mail: {1}\n\nMessage: {2}".format(name, email, message)

    try :
        mail.send(msg)

        message = "Message successfully sent!"
        code = 200
    except:
        message = "Message could not send!"
        code = 201
    
    return make_response(jsonify(
        response={
            'message':  message,
            'statusCode': code
        }
    ), code)


'''}
##################################################################################################
###################################### End Application Routes ####################################
##################################################################################################
'''


###################################
# Main function where app is run. #
###################################
if __name__ == "__main__":
    public = "0.0.0.0"
    local = "127.0.0.1"
    app.secret_key = "something"
    
    app.run(host=public, threaded=True)
    # app.run()

