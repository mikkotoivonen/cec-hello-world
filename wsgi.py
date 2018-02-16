import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    hostname = socket.gethostname()
    timestamp = str(datetime.now())
    return "Hello World! Greetings from "+hostname + " " +timestamp+"\n"


if __name__ == "__main__":
    application.run()
