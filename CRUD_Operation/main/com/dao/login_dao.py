from main import db
from main.com.vo.login_vo import LoginVO

class LoginDAO:

    def insert_user(self,login_vo):
        db.session.add(login_vo)
        db.session.commit()

    def login_list(self,email):
        login_list = LoginVO.query.filter_by(login_email = email)
        return login_list


