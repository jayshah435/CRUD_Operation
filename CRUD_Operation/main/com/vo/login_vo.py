from main import db

class LoginVO(db.Model):
    __tablename__ = 'login_table'
    login_id = db.Column('login_id', db.Integer, primary_key=True, autoincrement=True)
    login_username = db.Column('login_username', db.String(255),
                               nullable=False)
    login_email = db.Column('login_email', db.String(255),
                               nullable=False)
    login_password = db.Column('login_password', db.String(255),
                               nullable=False)

    def as_dict(self):
        return {
            'login_id': self.login_id,
            'login_username': self.login_username,
            'login_email': self.login_email,
            'login_password': self.login_password
        }

db.create_all()