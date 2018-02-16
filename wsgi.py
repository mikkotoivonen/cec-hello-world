import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    file = open("/mnt/log","w")
    file.write(timestamp + ":" + hostname +  "\n")
    file.close()
    return "Hello World! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
