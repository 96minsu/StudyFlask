# Current_app으로 현재 구동되는 어플리케이션 확인할 수 있음
from hello4 import app as app4
from hello2 import app as app2
from flask import current_app

app_ctx = app4.app_context()
app_ctx.push()
print(current_app.name)
app4.run()
