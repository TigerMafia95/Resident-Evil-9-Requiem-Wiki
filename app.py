import mariadb
from flask import Flask, render_template

app = Flask(__name__)

conn = mariadb.connect(
    user="root",
    password="12345",
    host="localhost",
    database="re9wiki"
)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)