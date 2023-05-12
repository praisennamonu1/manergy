from . import main_bp
from flask import render_template

@main_bp.get('/')
def index():
    return render_template('main/dashboard.html')