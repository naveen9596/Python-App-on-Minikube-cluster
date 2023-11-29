from flask import Flask
app = Flask(__name__)

@app.route("/")
def hellohome():
    return "Hello Python home!"

@app.route("/app")
def helloapp():
    return "Hello Python app!"

@app.route("/test")
def hellotest():
    return "Hello Python test!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')