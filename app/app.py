from flask import Flask, render_template, redirect

from models import database
from login import login_bp

app = Flask(__name__)

# config を設定ファイルから読み込む
app.config.from_object('config.DevelopmentConfig')

# データベースの初期化
database.init_db(app)
app.register_blueprint(login_bp)

@app.route("/")
def home():
    return redirect('login')

if __name__ == '__main__':
    app.run()
