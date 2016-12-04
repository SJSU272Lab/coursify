import json
import sys
from pprint import pprint

filename = sys.argv[1]

with open(filename) as data_file:    
    data = json.load(data_file)

for row in data:
    for column in row:
        if not (len(row[column]["prereq"]) == 0):
            for prereq in row[column]["prereq"]:
              print "insert into prerequisite(dept_name, primary_course, prereq_course) values('Software engineering','%s', '%s');" % (str(column), str(prereq))
        if not (len(row[column]["coreq"]) == 0):
            for coreq in row[column]["coreq"]:
              print """insert into corequisite(dept_name, primary_course, coreq_course) values("Software engineering","%s", "%s");""" % (str(column), str(coreq))