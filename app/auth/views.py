from . import auth_bp
from flask import render_template
from .forms import SignUpForm


@auth_bp.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('auth/signup.html', form = form)