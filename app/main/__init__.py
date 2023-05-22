from flask import Blueprint
from ..models import Video
from .controller import MainController

# create a new blueprint for the main features
main_bp = Blueprint('main', __name__)

# initialize the main controller
main_controller = MainController()


# populate the videos table in the db
@main_bp.before_request
def before_request():
    # fetch and save youtube videos
    print('Fetching videos from youtube...')
    main_controller.fetch_yt_videos(main_controller.default_kw)
    print('Fetched videos from youtube.')
    main_controller.save_videos()

from . import views