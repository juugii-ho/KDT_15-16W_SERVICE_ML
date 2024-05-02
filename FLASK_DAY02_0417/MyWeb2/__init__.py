from flask import Flask, render_template, url_for

def create_app():
    ## Flask Server 인스턴스 생성
    app = Flask(__name__)

    from flask import Blueprint
    from .views import data_view

    app.register_blueprint(data_view.dataBP)

    # @app.route('/input/')
    # def index():
    #     return render_template('input_data.html')

    return app
