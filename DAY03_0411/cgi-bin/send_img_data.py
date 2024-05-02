#!/usr/bin/env python


### 모듈 로딩
import cgi, sys, codecs, os
import datetime

# 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서 저장하고 있는 인스턴스
form = cgi.FieldStorage() # 대문자 시작 = 클래스

# 클라이언트의 요청 데이터 추출
if 'img_file' in form and 'message' in form:
    fileitem = form['img_file']  # == form.getvalue('img_file')

    # 서버에 이미지 파일 저장
    img_file = fileitem.filename        # == form.getvalue('message')

    suffix=datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    save_path = f'./image/{suffix}_{img_file}'
    with open(save_path, 'wb') as f:
        f.write(fileitem.file.read())

    img_path=f"../image/{img_file}"
    msg = form.getvalue('message')

else:
    img_path = "None"
    msg = "None"

sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


# 요청에 대한 응답 HTML
print("Content-Type: text/html; charset=utf-8 ")
print()                                         # 헤더와 바디 구분
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
# print(f"Hello, world! : {form}")
# print()
print(f"<img src={img_path}>")
print(f"<h3> {msg} </h3>")