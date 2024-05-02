### ===> 기능 : main 범주의 URL 라우팅 처리
### ===> URL : /main, /main/info, /main/about, ... 

from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/main/')

@bp.route('about')
def main_about():
    return "ABOUT MAIN"