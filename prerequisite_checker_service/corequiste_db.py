from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://userdbcmpe281:cmpe281project@mydb-cmpe281.csijd9oqjoza.us-west-2.rds.amazonaws.com/272project'
db = SQLAlchemy(app)

class Corequisite(db.Model):
    __tablename__ = "corequisite"
    id = db.Column('id', primary_key=True)  
    dept_name = db.Column(db.String(80))
    coreq_course = db.Column(db.String(100))
    primary_course = db.Column(db.String(200))


    def __init__(self, dept_name, coreq_course, primary_course):
        self.dept_name = dept_name
        self.coreq_course = coreq_course
        self.primary_course = primary_course
        
