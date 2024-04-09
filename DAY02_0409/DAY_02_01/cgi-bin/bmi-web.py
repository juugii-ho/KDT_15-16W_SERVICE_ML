"""
# URL : http://localhost:8080/cgi-bin/bmi_web.py
"""

### ==> 모듈 로딩
import cgi, sys, codecs, os, cgitb
import cgitb
from pydoc import html
# import job

cgitb.enable()

### ==> Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()

sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())

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