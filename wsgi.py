from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World Rowland Ekemezie!"

if __name__ == "__main__":
    application.run()
