# 에러 catch 및 throw
# 에러에 대한 처리

# 에러 catch 처리
@app.errorhandler(403)
def page_forbidden(error):
    print 'Hey ! You are not allowed to acces this !'

@app.errorhandler(403)
def page_not_found(error):
    print 'Ho no ! The ressource you want to access does not exist :('

# 에러 throw 처리
@app.route('/show_account_infos')
def show_account_infos():
    if not user.logged_in:
        abort(401)

        # Do things ...