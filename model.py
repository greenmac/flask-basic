from hello_flask import db

class UserReister(db.Model):
    """記錄使用者資料的資料表"""
    __tablename__ = 'UserRgeisters' # 若沒設置會以類別名稱為資料表名稱
    id = db.Column(db.Integer, primark_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'username:%s, email:%s' % (self.username, self.email)