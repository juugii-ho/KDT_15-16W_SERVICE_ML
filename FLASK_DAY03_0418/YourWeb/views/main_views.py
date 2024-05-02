from flask import Blueprint, render_template, request
from ..models import Question, Answer
from datetime import datetime

bp = Blueprint('main',
               __name__,
               template_folder='templates',
               url_prefix='/')

## 라우팅 함수들
@bp.route('/')
def index(): 
    # Question 테이블에 저장된 데이터 읽어서 출력
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('q_list.html', question_list=question_list)

@bp.route('/question/create')
def create_question():
    return render_template('q_create.html')

@bp.route('/question/answer', methods=['POST'])
def create_answer():
    text = request.form['text']
    email = request.form['email']
    return render_template('q_answer.html', text=text, email=email)