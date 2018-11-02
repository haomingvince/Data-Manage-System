# model.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:19970920@localhost/sys?charset=UTF8MB4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
db.init_app(app)
# To create table: run db.create_all()
# Reference to: https://blog.csdn.net/lilovfly/article/details/78513311


def db_init():
    db.create_all()
    return


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def delete(self, username):  # TODO: Bug fix needed!
        try:
            self.query.filter_by(username=username).delete()
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def update(self, username, newpwd):
        try:
            self.query.filter_by(username=username).update({'password': newpwd})
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def ifExist(self):
        temp = User.query.filter_by(username=self.username).first()
        if temp is None:
            return 0
        else:
            return 1

    def chkPwd(self):
        temp = User.query.filter_by(username=self.username, password=self.password).first()
        if temp is None:
            return 0
        else:
            return 1


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(32))
    sendby = db.Column(db.String(32))

    def __init__(self, contents, sendby):
        self.contents = contents
        self.sendby = sendby

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def delete(self, contents):  # TODO: Bug fix needed!
        try:
            self.query.filter_by(contents=contents).delete()
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0