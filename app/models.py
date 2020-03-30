from app import db


class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(64), unique=True)
    building = db.Column(db.String(64))
    budget = db.Column(db.Numeric(12, 2))


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    dept_name = db.Column(db.String(64), db.ForeignKey('departments.dept_name'))
