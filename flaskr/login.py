
## Main 작성 1
# 표준이 되는 메인 작성
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask import Flask, request, render_template

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

app = Flask(__name__)
app.config.from_object(__name__)

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

## Main 작성 2
# 실제 form 처리 함수 작성
@app.route('/loginform', methods=["POST"])
def form_proc():
    rst = "form success"
    if request.method == "POST" :
        openid = request.form['openid']
        remember_me = request.form['remember_me']
        
    return rst+'openid: ' + openid + 'remember_me: ' + str(remember_me)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
