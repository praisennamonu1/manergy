from . import auth_bp
from flask import render_template, request, redirect, url_for, flash
from ..models import User, db
import datetime
from flask_login import login_user, current_user, login_required, logout_user


@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    return render_template('auth/login.html')

@auth_bp.post('/signup')
def signup():
    try:
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
    except Exception as e:
        flash(str(e), 'error')
    finally:
        # on error
        return redirect(url_for('.index'))


@auth_bp.post('/login')
def login():
    """Log the user if the user has an account."""
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        # check if required fields are set
        if (all([email, password])):
            user = User.get_one_by(email=email)
            # if user was found and password is valid, login user
            if user is not None and user.verify_password(password):
                login_user(user, True, datetime.timedelta(1.5)) # log user in using flask login manager

                # get the query parameter, next
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                
                flash('Welcome! I hope you will enjoy the moments you spend here.')
                return redirect(next)
            else:
                flash('Invalid email or password', 'error')
        else:
                # handle invalid form data
                flash('Please fill in all the required fields.', 'error')
    except Exception as e:
        flash(str(e), 'error')
    finally:
        return redirect(url_for('.index'))
    

@auth_bp.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('auth.index'))