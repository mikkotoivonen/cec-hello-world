import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    
    file = open("mnt/log","r")
    out = file.read()
    file.close()
    return out


if __name__ == "__main__":
    application.run()
    hostname = socket.gethostname()
    timestamp = str(datetime.now())
    file = open("/mnt/log","a")
    file.write(timestamp + ":" + hostname +  "\n")
    file.close()
