from . import auth_bp
from flask import render_template


@auth_bp.get('/')
def index():
    return render_template('auth/login.html')