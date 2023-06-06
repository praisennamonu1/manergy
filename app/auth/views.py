from . import auth_bp
from flask import render_template, request, redirect, url_for, flash
from ..models import User, db
from flask_login import login_user, current_user


@auth_bp.route('/', methods=['GET', 'POST'])
def index():
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
                new_user = User(firstname=fname, lastname=lname,
                                email=email, password=password)
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
        return redirect(url_for('.index'))


@auth_bp.post('/login')
def login():
    """Log the user if the user has an account."""
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        if current_user.is_authenticated:
            return redirect(url_for('main.index'))

        # check if required data is given
        if all([email, password]):
            # create user
            user = User.get_one_by(email=email)
            if user and user.verify_password(password):
                login_user(user, True, 3600 * 24)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                flash('Welcome! I hope you will enjoy the moments you spend here.')
                return redirect(next)
            flash('Invalid email or password', 'error')
    except Exception as e:
        flash(str(e), 'error')
    finally:
        return redirect(url_for('.index'))
