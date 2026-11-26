from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzueg.security import generate_password_hash, check_password_hash
import pymysql
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        firstname = request.form["firstname"].strip()
        lastname = request.form["lastname"].strip()
        email = request.form["email"].lower().strip()
        phone = request.form["phone"].strip()
        username = request.form["username"]
        password = request.form["password"]
        confirmpassword = request.form["confirmpassword"]
        if not firstname or not lastname or not email or not phone or not username or not password or not confirmpassword:
            flash("Inputs cannot be empty")
            return render_template("signup.html")
        if len(password) < 8:
            flash("Password must be at least 8 characters")
            return render_template("signup.html")
        if password != confirmpassword:
            flash("Passwords do not match")
            return render_template("signup.html")
        if '@'  not in email or '.' not in email.split('@')[1]:
            flash("Invalid email format")
            return render_template("signup.html")
        if (
            not any(c.islower() for c in password)
            or not any(c.isupper() for c in password)
            or not any(c.isdigit() for c in password)
            or not any(not c.isalnum() for c in password)
        ):
            flash("Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character")
            return render_template("signup.html")

        conn = Config.SQLALCHEMY_DATABASE_URI
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (firstname, lastname, email, phone, username, password_hash"
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (firstname, lastname, email, phone, username, generate_password_hash(password))
                )
            conn.commit()
        except pymysql.err.IntegrityError:
            flash("Username or email already exist")
            return render_template("signup.html")
        finally:
            conn.close
        return redirect(url_for("login"))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"].strip
        password = request.form["password"]

        conn = Config.SQLALCHEMY_DATABASE_URI
        with conn.cursor() as cur:
            conn.execute(
                "SELECT id, username, password_hash From users WHERE username = %s",
                (username,),
            )
            user = cur.fetchone()
        conn.close()
        
        if user and check_password_hash(user["password_hash"], password): 
            session.clear() 
            session["user_id"] = user["id"] 
            session["username"] = user["username"] 
            return redirect(url_for("index"))



    return render_template('login.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/memberships')
def memberships():
    return render_template('memberships.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

if __name__ == '__main__':
    app.run(debug=True)


