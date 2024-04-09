#!/usr/bin/env python
# 맥에서는 리눅스 명령어로 지정해줘야 함
# 폴더와 파일에 권한도 줘야함  chmod +x /cgi-bin/index_01.py 


### ==> 모듈 로딩
import cgi

### ==> Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()

### ==> 데이터 추출
if 'data' in form and 'no' in form:
    result=form.getvalue('data') + " - " + form.getvalue('no')
else:
    result="No Data"


### ==> Web 브라우저 화면 출력 코드
def print_browser(result=""):
    # HTML Header
    filename="../html/test.html"
    with open(filename, 'r', 'utf-8') as f:
        print("Content-Type: text/html; charset=utf-8-sig")
        print()

        # HTML Body
        # f.read().format(result)
        print(f.read().format(result))