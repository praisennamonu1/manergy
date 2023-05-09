from flask_login import LoginManager
from ..models import User, AnonymousUser

login_mgr = LoginManager()

# setup the user loader
@login_mgr.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

# make flask login aware of the custom anonymous user class
login_mgr.anonymous_user = AnonymousUser

