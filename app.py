# import main Flask class and request object
from flask import Flask, request
from multiprocessing import Process
import displayMessage
import os
import psutil
import time
#dPid = None 
# create the Flask app
app = Flask(__name__)
@app.route('/display-time', methods = ['POST'])
def clock_display():
    message = request.args.get('message')
    if(message=='stop'):
        displayMessage.exitLoop="set"
        return message
    return displayMessage.displayClock()
    

@app.route('/display-message', methods = ['POST'])
def display_single_message():
    message = request.args.get('message')
    displayMessage.exitLoop="set"
    displayMessage.displayMessage(message)
    time.sleep(5)
    displayMessage.displayClock()
    return message

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
