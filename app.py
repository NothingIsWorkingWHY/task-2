from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
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


