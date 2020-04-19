from flask import Flask

app = Flask(__name__)

def index():
    return "Hello, World!!!!!!!"

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
