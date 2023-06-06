from . import main_bp
from flask import render_template
from ..models import Video


@main_bp.get('/')
def index():
    return render_template('main/index.html')


@main_bp.get('/mental-energy')
def mental_energy():
    # fetch videos that discussed mental energy from db
    videos = Video.get_by_attrs(keyword='Mental Energy')
    print(videos)

    return render_template('main/mental-energy.html', videos=videos)


@main_bp.route('/physical-energy', methods=['GET', 'POST'])
def physical_energy():
    return render_template('main/physical-energy.html')
