
## Login 프로그램 작성
# Login에서 GET 메소드로 login login 폼을 전달해서 Post 메소드로 값을 넣고 재처리
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    #GETreques'
    if request.method=='GET':
        return render_template('login_1.html')
    #POSTREQUEST
    else:
        email=request.form['email']
        password=request.form['password']
        #Checkmail&password
        #TODO
        return "email" + email + "password" + str(password)
    
if __name__ == '__main__':
    app.run(debug=True)
