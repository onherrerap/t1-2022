from flask import Blueprint, render_template

# ブル-プリントをインスタンス化
user_info_bp = Blueprint('user_info', __name__, url_prefix='/user_info')

# ユーザーネーム変更ページを表示
@user_info_bp.route('/change_name')
def change_user_name():
    return render_template('change_user_info/change_user_name.html')

# ユーザーパスワード変更ページを表示
@user_info_bp.route('/change_passwd')
def change_user_passwd():
    return render_template('change_user_info/change_user_passwd.html')

# ユーザーメールアドレス変更ページを表示
@user_info_bp.route('/change_mail')
def change_user_mail():
    return render_template('change_user_info/change_user_mail.html')