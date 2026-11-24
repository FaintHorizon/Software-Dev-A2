import flask
import time
import sqlite3

app = flask.Flask(__name__, template_folder=".")


# ---- Main Page ----

@app.route("/")
def index():
    return flask.render_template("index.html")


# ---- Forum Page ----

@app.route("/main")
def main():
    return flask.render_template("main.html")


# ---- Coming Soon Page ----

@app.route("/CS")
def comingSoon():
    return flask.render_template("CS.html")


# ---- Run Application ----

if __name__ == "__main__":
    app.run(debug=True)
