from flask import *
from main import app
from main.com.vo.login_vo import LoginVO
from main.com.dao.login_dao import LoginDAO


@app.route('/')
def home():
    try:
        return render_template("login.html")
    except Exception as e:
        return e

@app.route('/register')
def register():
    try:
        return render_template("register.html")
    except Exception as e:
        return e

@app.route('/insert_login', methods=['POST'])
def insert_login():
    try:
        email = request.form.get('email')
        username = request.form.get('userName')
        password = request.form.get('password')

        login_vo = LoginVO()
        login_dao = LoginDAO()

        login_vo.login_email = email

        login_list = login_dao.login_list(login_vo.login_email)

        user_list = [i.as_dict() for i in login_list]
        t_list = len(user_list)

        if t_list == 0:
            login_vo.login_email = email
            login_vo.login_username = username
            login_vo.login_password = password
            login_dao.insert_user(login_vo)

            return render_template("login.html")
        else:
            error_msg = "User is already exist!"
            flash(error_msg)
            return redirect('/register')


    except Exception as e:
        return e

@app.route("/validate_login", methods=['POST'])
def validate_login():
    try:
        user_mail = request.form.get('text')
        password = request.form.get('password')

        if user_mail == "jayshah@abc.com" and password == "jayshah":
            return render_template("admin/home.html")

        else:
            # print(user_mail)
            # print(password)
            login_vo = LoginVO()
            login_vo.login_email = user_mail

            login_dao = LoginDAO()
            login_list = login_dao.login_list(login_vo.login_email)
            # print(login_list)

            user_list = [i.as_dict() for i in login_list]
            # print(user_list)

            t_list = len(user_list)

            if t_list == 0:
                error_msg = "Email Or Mobile No Is Incorrect !"
                flash(error_msg)
                return redirect('/')
            else:
                user_password = user_list[0]['login_password']

                if user_password != password:
                    error_msg = "Password Is Incorrect!"
                    flash(error_msg)
                    return redirect('/')
                else:
                    login_username = user_list[0]['login_username']
                    return render_template("User/homePage.html",
                                           login_username= login_username)


    except Exception as e:
        return e



