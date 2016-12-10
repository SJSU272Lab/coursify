from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql:///college_courses'
app.config['SQLALCHEMY_POOL_SIZE'] = 3
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
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
        
