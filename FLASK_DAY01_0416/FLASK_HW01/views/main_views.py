from flask import Blueprint, url_for, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('about')
def main_about():
    return render_template('index.html')
