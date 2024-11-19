from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_from_directory,
)
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"


# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def register_user(username, password, email):
    conn = get_db_connection()
    cursor = conn.cursor()

    username = username.lower()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone() is not None:
        print("Username already exists.")
        conn.close()
        return False

    hashed_password = generate_password_hash(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, hashed_password, email),
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()


# Function to login a user
def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row and check_password_hash(row["password"], password):
        return True
    else:
        return False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<path:path>")
def send_static(path):
    return send_from_directory("templates", path)


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    if register_user(username, password, email):
        flash("Registration successful! You can now log in.", "success")
    else:
        flash("Username already exists. Please choose a different one.", "error")

    return redirect(url_for("home"))


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if login_user(username, password):
        flash("Login successful!", "success")
        return redirect(url_for("home"))  # Change this to your desired route
    else:
        flash("Invalid credentials. Please try again.", "error")

    return redirect(url_for("home"))


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
