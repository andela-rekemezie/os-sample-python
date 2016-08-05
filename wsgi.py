from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "hell man!"

@application.route("/login")
def login():
		return "This is the Loging page. Josh, please login"

if __name__ == "__main__":
    application.run()
