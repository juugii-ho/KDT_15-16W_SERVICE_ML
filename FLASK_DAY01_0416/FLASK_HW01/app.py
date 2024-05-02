# ### 모듈 로딩
from flask import Flask, Blueprint

def create_app():
    hwapp = Flask(__name__)

    # bp 등록
    from .views import main_views
    hwapp.register_blueprint(main_views.bp)

    return hwapp