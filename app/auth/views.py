from . import auth_bp
from flask import render_template, request, redirect, url_for, flash
from ..models import User, db


@auth_bp.get('/')
def index():
    return render_template('auth/login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # check if required data is given
    
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
        
    if fname and lname and email and password and (password == confirm_password):
        user = User(firstname=fname, lastname=lname, email=email, password=password)
        # save the user to the database
        db.session.add(user)
        db.session.commit()
        # redirect to dashboard
        return redirect(url_for('main.dashboard'))
    else:
            # handle invalid form data
            flash('Please fill in all the required fields and ensure that your password and confirmation match.')
    
    return render_template('auth/login.html')