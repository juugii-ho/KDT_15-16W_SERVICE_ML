# ### 모듈 로딩
from flask import Flask, render_template, Blueprint


### 애플리케이션 팩토리 함수
def create_app():
    myapp = Flask()

    # bp 등록
    from .views import main_views            # 위치가 중요
    myapp.register_blueprint(main_views.bp)

    return myapp



# ### 전역변수
# myapp = Flask(__name__)


# ### 사용자 요청 URL 처리 기능 => 라우팅(Routing)
# ### 형식 : @Flask_instance_name.route(URL 문자열)

# # 웹서버의 첫 페이지 : http://127.0.0.1:5000/ => '/'로 축약해서 적음
# @myapp.route('/')
# def index_page():
#     # return "<h3><font color='green'>My Web Index Page</font></h3>"
#     return render_template('tem.html')

# ### 사용자마다 페이지 반환
# ### 사용자 페이지 URL : http://127.0.0.1:5000/<username>
# @myapp.route('/<username>')  # 홑화살괄호를 하지 않으면 변수로서가 아닌 문자열로서 username만 인식
# def username(name):
#     return f"username : {name}"

# @myapp.route('/<int:number>')
# def show_number(number):
#     return f"Select Number : {number}"

# @myapp.route('/hello/')   # 마지막에 /가 있으면 주소창 마지막에 /가 없더라도 폴더or파일로 인식해서 붙여줌
# def hello():              #        /가 없으면 주소창 마지막에 /가 없어도 안 붙여줌
#     return "hello"        #     => 마지막에 /가 있고 없고를 다른 경우로 인식함

# @myapp.route('/about')
# def about():
#     return 'A.B.O.U.T'

# @myapp.route('/projects/')
# def show_project():
#     return '=> project ___'

# @myapp.route('/user_info2')
# def user_login2():
#     return myapp.redirect('/')

# ### 실행 제어
# if __name__ == '__main__':
#     # Flask 웹 서버 구동
#     myapp.run()

