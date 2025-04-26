from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, There I am Somay Verma!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
