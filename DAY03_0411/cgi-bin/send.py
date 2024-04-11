#!/usr/bin/env python


### 모듈 로딩
import cgi, sys, codecs, os

# 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서 저장하고 있는 인스턴스
form = cgi.FieldStorage() # 대문자 시작 = 클래스

# 클라이언트의 요청 데이터 추출
if 'img_file' in form and 'message' in form:
    filename = form['img_file']  # == form.getvalue('img_file')
    msg = form['message']        # == form.getvalue('message')


sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


# 요청에 대한 응답 HTML
print("Content-Type: text/html; charset=utf-8 ")
print()                                         # 헤더와 바디 구분
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print(f"Hello, world! : {form}")
print()
print(f"<img src={filename}>")
print(f"<h3> {msg} </h3>")