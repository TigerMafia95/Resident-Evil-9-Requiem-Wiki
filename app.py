import mariadb
from flask import Flask, render_template

app = Flask(__name__)

# -------------------------
# DATABASE CONFIG (YOUR INFO KEPT)
# -------------------------
DB_CONFIG = {
    "user": "root",
    "password": "12345",
    "host": "localhost",
    "database": "re9wiki"
}

# -------------------------
# SAFE DB CONNECTION FUNCTION
# -------------------------
def get_db_connection():
    try:
        return mariadb.connect(**DB_CONFIG)
    except mariadb.Error as e:
        print(f"Database connection error: {e}")
        return None


# -------------------------
# ROUTES
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/characters")
def characters():
    conn = get_db_connection()

    # optional: later you can fetch from DB
    # for now just template works safely
    if conn:
        conn.close()

    return render_template("characters.html")


@app.route("/story")
def story():
    return render_template("story.html")


@app.route("/enemies")
def enemies():
    return render_template("enemies.html")


@app.route("/weapons")
def weapons():
    return render_template("weapons.html")


@app.route("/FAQ")
def faq():
    return render_template("FAQ.html")



# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)