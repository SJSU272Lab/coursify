from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://userdbcmpe281:cmpe281project@mydb-cmpe281.csijd9oqjoza.us-west-2.rds.amazonaws.com/272project'
db = SQLAlchemy(app)

class Prerequisite(db.Model):
    __tablename__ = "prerequisite"
    id = Column('id', primary_key=True)  
    dept_name =  Column(VARCHAR(80), nullable=False)
    prereq_course = Column(VARCHAR(80), nullable=False)
    primary_course = Column(VARCHAR(80), nullable=False)


    def __init__(self, dept_name, prereq_course, primary_course):
        self.dept_name = dept_name
        self.prereq_course = prereq_course
        self.primary_course = primary_course