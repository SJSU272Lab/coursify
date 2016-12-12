import logging
import json
import os
import sys
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import feedbackAnalyser as fa


def getCourseDict(name, course, prof):
    name, prof, course = str(name), str(prof), str(course)
    _id = course + "_" + prof
    _id = _id.replace(' ', '_')
    # logging.debug("course:'%s' prof:'%s' id:'%s'" % (course, prof, _id))
    return {"name": name,
            "course": course,
            "prof": prof,
            "id": _id}


def recommendMajorSubjets(major, techLiking):
    # TODO store data in DB and get it from there
    # TODO use techLiking to pick prof
    if major == "Cloud computing and virtualization":
        # return [getCourseDict(name="Cloud Technologies",
        #                       course="CMPE281",
        #                       prof=""),
        #         getCourseDict(name="Virtualization Technologies",
        #                       course="CMPE283",
        #                       prof="")]
        return ["CMPE281", "CMPE283"]
    if major == "Software systems Engineering":
        # return [getCourseDict(name="Software Engineering Processes",
        #                       course="CMPE285",
        #                       prof=""),
        #         getCourseDict(name="Software Quality Assurance and Testing",
        #                       course="CMPE287",
        #                       prof="")]
        return ["CMPE285", "CMPE287"]
    if major == "Enterprise Software Technologies":
        # return [getCourseDict(name="Enterprise Distributed Systems",
        #                       course="CMPE273",
        #                       prof=""),
        #         getCourseDict(name="Enterprise Application Development",
        #                       course="CMPE275",
        #                       prof="")]
        return ["CMPE273", "CMPE275"]
    if major == "Networking Software":
        # return [getCourseDict(name="Computer Network Design",
        #                       course="CMPE206",
        #                       prof=""),
        #         getCourseDict(name="Network Programming and Applications",
        #                       course="CMPE207",
        #                       prof="")]
        return ["CMPE206", "CMPE207"]


def recommendMinorSubjet(major, techLiking):
    # TODO store data in DB and get it from there
    # TODO use techLiking to pick prof and either of the two subjects
    if major == "Cloud computing and virtualization":
        # return getCourseDict(name="Cloud Technologies",
        #                      course="CMPE281",
        #                      prof="")
        return "CMPE281"
    if major == "Software systems Engineering":
        # return getCourseDict(name="Software Engineering Processes",
        #                      course="CMPE285",
        #                      prof="")
        return "CMPE285"
    if major == "Enterprise Software Technologies":
        # return getCourseDict(name="Enterprise Distributed Systems",
        #                      course="CMPE273",
        #                      prof="")
        return "CMPE273"
    if major == "Networking Software":
        # return getCourseDict(name="Computer Network Design",
        #                      course="CMPE206",
        #                      prof="")
        return "CMPE206"


# TODO move this function to a separate module
def getPreReqs(department):
    # TODO store data in DB and get it from there
    if department == "Software Engineering":
        return [getCourseDict(name="Operating Systems",
                              course="CMPE180-38",
                              prof="Hungwen Li"),
                getCourseDict(name="Database Design",
                              course="CMPE180-94",
                              prof="Kong Li"),
                getCourseDict(name="Object Oriented Programming"
                                   " and Data Structure",
                              course="CMPE180-92",
                              prof="Ron Mak")]


def recommendCoreSubjects(department, techLiking):
    # TODO store data in DB and get it from there
    # TODO use techLinking and select prof, hardcoding for now
    if department == "Software Engineering":
        # TODO recommend prof
        # return [getCourseDict(name="Software Systems Engineering",
        #                       course="CMPE202",
        #                       prof="Paul Nguyen"),
        #         getCourseDict(name="Enterprise Software Platforms",
        #                       course="CMPE272",
        #                       prof="Rakesh Ranjan")]
        return ["CMPE272", "CMPE202"]


def getCulmExpCourses(department, culminatingExp):
    if department == "Software Engineering":
        if culminatingExp == "Master Project I and II":
            # return [getCourseDict(name="Master Project I",
            #                       course="CMPE295A",
            #                       prof="NA"),
            #         getCourseDict(name="Master Project II",
            #                       course="CMPE295B",
            #                       prof="NA")]
            return ["CMPE295A", "CMPE295B"]
        else:
            # return [getCourseDict(name="Master Thesis I",
            #                       course="CMPE299A",
            #                       prof="NA"),
            #         getCourseDict(name="Master Thesis II",
            #                       course="CMPE299B",
            #                       prof="NA")]
            return ["CMPE299A", "CMPE299B"]


def getAllElectives(department):
    # use a mapping config file, mapping department to their course JSON file
    # TODO use better variable names :P
    if department == "Software Engineering":
        cFile = os.path.join(os.path.dirname(__file__), "CMPE-courses.json")
        with open(cFile) as fp:
            courses = json.load(fp)
        e = []
        for course in courses:
            if course not in ["CMPE295A", "CMPE295B", "CMPE295W",
                              "CMPE299A", "CMPE299B"]:
                e.append(getCourseDict(course=course, name=courses[course],
                                       prof=""))
        return e


def getCourseName(course):
    # SE only
    cFile = os.path.join(os.path.dirname(__file__), "CMPE-courses.json")
    with open(cFile) as fp:
        courses = json.load(fp)
    return courses[course]


def getAllCoursesList(department="Software Engineering"):
    if department == "Software Engineering":
        cFile = os.path.join(os.path.dirname(__file__), "CMPE-courses.json")
        with open(cFile) as fp:
            courses = json.load(fp)
        return sorted([x for x in courses])


def weightSubjects(subjects, techLiking):
    # TODO use better variable names :P
    keys = fa._keys("CMPE*")
    logging.error("All keys:%s" % keys)
    subjectsWithData = []
    for key in keys:
        subjectsWithData.append(key.split('_')[0])
    # print subjectsWithData
    subjectsWithData = [x for x in set(subjectsWithData)]
    # print subjectsWithData
    # TODO filter subjectsWithData with only the ones in subjects
    subjectWeight = []
    for subject in subjectsWithData:
        # print subject
        score = fa.getCourseScore(subject)
        # print score
        # print techLiking
        weight = somefn(score, techLiking)
        # print weight
        subjectWeight.append((subject, weight))
        # print "-" * 80
    a = filter(lambda x: x[0] in subjects, subjectWeight)
    b = [x[0] for x in a]
    for x in subjects:
        if x not in b:
            a.append((x, 0))
    return a


# TODO use better name :P
def somefn(score, techLiking):
    weight = 0
    for tech in techLiking:
        x = score.get(tech, None)
        if x:
            weight += x["value"]
    return weight


def filterCourses(courses, exp):
    return [course for course in courses if course[0] not in exp]


def getTopCourses(courses, count=None):
    m = sorted(courses, lambda x, y: cmp(-x[1], -y[1]))
    m = m[:count]
    fa.pprint(m, "MMMM")
    return m


def recommendElectives(techLiking, department, count=None, exp=[]):
    electives = getAllElectives(department)
    # Get just the course name
    electives = [x['course'] for x in electives]
    wElectivies = weightSubjects(electives, techLiking)
    wElectivies = filterCourses(wElectivies, exp)
    wElectivies = getTopCourses(wElectivies, count)
    electives = [e[0] for e in wElectivies]
    fa.pprint(electives, "electives and weight")
    return electives


def getConstraints(sub):
    # TODO store url in a config file
    url = "http://ec2-35-162-102-240.us-west-2.compute.amazonaws.com/" \
          "prerequisite_check?course=CMPE%20" + sub[4:]
    response = requests.get(url)
    data = response.json()
    prereqs = [x[:4] + x[5:] for x in data['prereq']]
    coreqs = [x[:4] + x[5:] for x in data['coreq']]
    logging.info("For sub %s:" % sub)
    logging.info("Prereqs: %s" % prereqs)
    logging.info("Coreqs: %s" % coreqs)
    return prereqs, coreqs


def getSemwiseSubjects(someDic):
    orderedSubs = someDic['preReqs'] + \
        someDic['coreSubjects'] + \
        someDic['majorSubjects'] + \
        someDic['minorSubjects']

    independantSubs = []
    dependantSubs = []
    for sub in someDic['electives']:
        preReqs, coReqs = getConstraints(sub)
        constraints = preReqs + coReqs
        flag = False
        for contraint in constraints:
            if contraint not in orderedSubs + independantSubs + dependantSubs:
                # TODO
                # assuming prereqs themselves don't have prereqs themselves
                # will fix it later
                independantSubs.append(contraint)
                flag = True
        if flag:
            dependantSubs.append(sub)
        else:
            independantSubs.append(sub)
    updatedElectives = independantSubs + dependantSubs

    orderedSubs += updatedElectives[:3]

    if len(someDic['preReqs']) < 3:
        return [orderedSubs[:3],
                orderedSubs[3:6],
                orderedSubs[6:8] + [someDic['culmExpCourses'][0], ],
                orderedSubs[8:] + [someDic['culmExpCourses'][1], ]]
    else:
        return [orderedSubs[:4],
                orderedSubs[4:7],
                orderedSubs[7:9] + [someDic['culmExpCourses'][0], ],
                orderedSubs[9:] + [someDic['culmExpCourses'][1], ]]


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # fa.pprint(getAllElectives("Software Engineering"))
    print recommendElectives(techLiking=["docker", "elastic"],
                             department="Software Engineering",
                             count=10)
    # print getCourseName("CMPE273")
