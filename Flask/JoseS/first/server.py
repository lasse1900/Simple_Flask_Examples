from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():

    input("give me a number: ")
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)