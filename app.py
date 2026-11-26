from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
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
            flash("Password must be longer than 8 characters")
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
            or not any(c.isalnum() for c in password)
        ):
            flash("Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character")
            return render_template("signup.html")
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
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


