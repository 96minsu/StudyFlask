
## make_response
# response를 만들기 위해 make_response 함수를 처리
from flask import Flask, session, request, redirect, url_for, \make_response

print("name: ", __name__)

app = Flask(__name__)

#set the secret key. Keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def index():
    response = make_response("<h1>Hello, World!!!!!!! </h1>")
    return response

app.add_url_rule('/', 'index', index)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
print(app.url_map)
            
if __name__ == '__main__':
    app.run(debug=True)
