from manergy import app
from flask import render_template
from manergy.forms import SignUpForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username='Preno')

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form = form)