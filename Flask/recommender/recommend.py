import logging


def getCourseDict(name, course, prof):
    _id = course + "_" + prof
    _id = _id.replace(' ', '_')
    logging.debug("course:'%s' prof:'%s' id:'%s'" % (course, prof, _id))
    return {"name": name,
            "course": course,
            "prof": prof,
            "id": _id}


def recommendMajorSubjets(major, techLiking):
    # TODO use techLiking to pick prof
    if major == "Cloud computing and virtualization":
        return [getCourseDict(name="Cloud Technologies",
                              course="CMPE281",
                              prof=""),
                getCourseDict(name="Virtualization Technologies",
                              course="CMPE283",
                              prof="")]
    if major == "Software systems Engineering":
        return [getCourseDict(name="Software Engineering Processes",
                              course="CMPE285",
                              prof=""),
                getCourseDict(name="Software Quality Assurance and Testing",
                              course="CMPE287",
                              prof="")]
    if major == "Enterprise Software Technologies":
        return [getCourseDict(name="Enterprise Distributed Systems",
                              course="CMPE273",
                              prof=""),
                getCourseDict(name="Enterprise Application Development",
                              course="CMPE275",
                              prof="")]
    if major == "Networking Software":
        return [getCourseDict(name="Computer Network Design",
                              course="CMPE206",
                              prof=""),
                getCourseDict(name="Network Programming and Applications",
                              course="CMPE207",
                              prof="")]


def recommendMinorSubjet(major, techLiking):
    # TODO use techLiking to pick prof and either of the two subjects
    if major == "Cloud computing and virtualization":
        return getCourseDict(name="Cloud Technologies",
                             course="CMPE281",
                             prof="")
    if major == "Software systems Engineering":
        return getCourseDict(name="Software Engineering Processes",
                             course="CMPE285",
                             prof="")
    if major == "Enterprise Software Technologies":
        return getCourseDict(name="Enterprise Distributed Systems",
                             course="CMPE273",
                             prof="")
    if major == "Networking Software":
        return getCourseDict(name="Computer Network Design",
                             course="CMPE206",
                             prof="")


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
        return [getCourseDict(name="Software Systems Engineering",
                              course="CMPE202",
                              prof="Paul Nguyen"),
                getCourseDict(name="Enterprise Software Platforms",
                              course="CMPE272",
                              prof="Rakesh Ranjan")]


def getCulmExpCourses(department, culminatingExp):
    if department == "Software Engineering":
        if culminatingExp == "Master Project I and II":
            return [getCourseDict(name="Master Project I",
                                  course="CMPE295A",
                                  prof="NA"),
                    getCourseDict(name="Master Project II",
                                  course="CMPE295B",
                                  prof="NA")]
        else:
            return [getCourseDict(name="Master Thesis I",
                                  course="CMPE299A",
                                  prof="NA"),
                    getCourseDict(name="Master Thesis II",
                                  course="CMPE299B",
                                  prof="NA")]


def recommendElectives(techLiking, count, exp):
    pass
