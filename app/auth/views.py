from . import auth_bp
from flask import render_template, request, redirect, url_for, flash
from ..models import User
from flask_login import login_user


@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('auth/login.html')

@auth_bp.post('/signup')
def signup():
    # extract form data
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
        
    # check if required data is given
    if all([fname, lname, email, password, confirm_password]):
        # check that password and check_password are equal
        if password != confirm_password:
            flash('Passwords not equal.', 'error')
        else:
            # create user
            new_user = User(firstname=fname, lastname=lname, email=email, password=password)
            new_user.save()
            # log user in
            login_user(new_user)
            # redirect to dashboard
            return redirect(url_for('main.index'))
    else:
        # handle invalid form data
        flash('Please fill in all the required fields.', 'error')
    # on error
    return redirect(url_for('.signup'))