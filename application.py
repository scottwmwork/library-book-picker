from flask import Flask, render_template
application = app = Flask(__name__)


# Basic app output
@app.route("/")
@app.route("/home")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()