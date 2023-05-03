from manergy import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username='Preno')