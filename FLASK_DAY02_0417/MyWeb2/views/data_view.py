## ------------------------------------------------------------------------------
## 역할 : 데이터 저장 및 출력관련 웹 페이지 라우팅 처리
## URL : /input
##       /input/save
##       /input/delete
##       /input/update
## ------------------------------------------------------------------------------
## 모듈로딩
from flask import Blueprint, render_template, request

## BP 인스턴스 생성
dataBP=Blueprint('data', __name__, template_folder='templates', url_prefix='/input')

## 라우팅 함수들
@dataBP.route('/')
def input_data():
    return render_template('input_data.html', 
                           action="/input/save", 
                           method="POST"
                           )


# ## GET 방식으로 데이터 저장 처리 함수
# ## 사용자의 요청 즉, request 객체에 데이터 저장되어 있음
# @dataBP.route('/save_get')
# def save_get_data():
#     # 요청 데이터 추출
#     req_dict = request.args.to_dict()
#     # v = req_dict.get('value')
#     # m = req_dict.get('message')
#     # return f"SAVE GET DATA : {req_dict}"
#     return render_template('save_data.html', **req_dict)


# # POST 방식으로 데이터 저장 처리 함수
# @dataBP.route('/save_post', methods=['POST'])
# def save_post_data():
#     # req_dict = request.form.to_dict()
#     headers=request.headers
#     method=request.method
#     args=request.args.to_dict()
#     v=request.form['value']
#     m=request.form['message']
#     return f'SAVE POST DATA = <br><br>METHOD : {method}<br><br>HEADERS : {headers}<br><br>ARGS : {args}<br><br>VALUE :{v}<br><br> MESSAGE : {m}'

# ###

@dataBP.route('/save', methods = ['GET', 'POST'])
def save_data():
    import cgi, sys, codecs, os
    import datetime

    if request.method == 'GET':
        req_dict = request.args.to_dict()
        return render_template('save_data.html', **req_dict)
    else:
        image_dir = os.path.abspath('MyWeb2/static/image')
        if not os.path.exists(image_dir):
            os.makedirs(image_dir, exist_ok=True)
        
        imgitem = request.files.get('img_file', None)
        print(imgitem)
        if imgitem and imgitem.filename != '':
            suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
            print(suffix)
            save_path = os.path.join(image_dir, f'{suffix}_{imgitem.filename}')
            print(save_path)
            try: 
                imgitem.save(save_path)
            except Exception as e:
                return str(e)

        headers=request.headers
        method=request.method
        args=request.args.to_dict()
        v=request.form['value']
        m=request.form['message']
        return f'SAVE POST DATA = <br><br>METHOD : {method}<br><br>HEADERS : {headers}<br><br>ARGS : {args}<br><br>VALUE :{v}<br><br> MESSAGE : {m}'


