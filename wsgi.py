import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():

    with open("/mnt/log", "a") as myfile:
        tmstmp = str(datetime.now())
        myfile.write(tmstmp+":"+socket.gethostname()+"<\br>\n")
        
    file = open("/mnt/log","r")
    out = file.read()
    file.close()
    return out+"\n"


if __name__ == "__main__":
    application.run()
