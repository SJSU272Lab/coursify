from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://userdbcmpe281:cmpe281project@mydb-cmpe281.csijd9oqjoza.us-west-2.rds.amazonaws.com/272project'
db = SQLAlchemy(app)

class Prerequisite(db.Model):
    __table__ = "Prerequisite"
    __tablename__ = 'prerequisite'
    dept_name = db.Column(db.String(80))
    prereq_course = db.Column(db.String(100))
    primary_course = db.Column(db.String(200))


    def __init__(self, dept_name, prereq_course, primary_course):
        self.dept_name = dept_name
        self.prereq_course = prereq_course
        self.primary_course = primary_course
        
    def __repr__(self):
        return '<Prerequisite %r>' % self.dept_name
        
    @property
    def toJson(self):
       return {
    "name" : self.dept_name,
    "email" : self.prereq_course,
    "category" : self.primary_course}
