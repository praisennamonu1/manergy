from . import main_bp
from flask import render_template

@main_bp.get('/')
def index():
    return render_template('main/index.html')

@main_bp.get('/mental-energy')
def mental_energy():
    return render_template('main/mental-energy.html')
