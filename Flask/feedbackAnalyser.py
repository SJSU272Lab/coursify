from recommender.techScore import getTechScore
from recommender.techScore import getTechList

import logging
import redis
import pickle

# TODO host redis separately
r = redis.StrictRedis(host='localhost', port=6379, db=0)


def analyse(feedback):
    techScore = getTechScore(feedback['review'])
    logging.debug("TecScore: %s" % techScore)
    pushToElastic(feedback)
    updateTechScore(course=feedback['course'],
                    professor=feedback['professor'],
                    techScore=techScore)


def pushToElastic(feedback):
    # TODO
    logging.info("#" * 10 + "TODO" + "#" * 10)
    logging.info("Pushing feedback to elastic")


def updateTechScore(course, professor, techScore):
    weightedTechScore = getProfCourseScore(course, professor)
    pprint(weightedTechScore, "Old tech score for %s under %s" % (course,
                                                                  professor))
    newWeightedTechScore = _addTechScore(weightedTechScore, techScore)
    _updateTechScore(course, professor, newWeightedTechScore)
    pprint(newWeightedTechScore, "New tech score for %s under %s" %
           (course, professor))
    return getProfCourseScore(course, professor)


def _addTechScore(weightedTechScore, newTechScore):
    w = weightedTechScore
    nw = dict()  # newWeightedTechScore
    for tech in w:
        # print tech
        nw[tech] = {}
        if tech in newTechScore:
            # pprint(tech, "tech")
            # pprint(w[tech]['value'], "w[tech]['value']")
            # pprint(w[tech]['n'], "w[tech]['n']")
            presentTotal = w[tech]['value'] * w[tech]['n']
            # pprint(presentTotal, "presentTotal")
            newTotal = presentTotal + newTechScore[tech]
            newAvg = newTotal / (w[tech]['n'] + 1)
            nw[tech]['value'] = newAvg
            nw[tech]['n'] = w[tech]['n'] + 1
        else:
            nw[tech]['value'] = w[tech]['value']
            nw[tech]['n'] = w[tech]['n']
    return nw


def _updateTechScore(course, professor, newTechScore):
    key = _getKey(course, professor)
    return _setter(key, newTechScore)


def _setter(key, value):
    """value must be a dict"""
    assert type(value) == dict, "Value inserted into Redis must be dict type"
    # TODO check if value satisfies schema
    pValue = pickle.dumps(value)
    r.set(key, pValue)


def __getter(key):
    """returns None OR dict"""
    val = r.get(key)
    if val is not None:
        val = pickle.loads(val)
        return val


def _getter(key):
    """returns dict ONLY"""
    # TODO add support for dynamically growing tech list
    val = __getter(key)
    if val is None:
        val = _getEmptyTechScore()
        assert val is not None
        _setter(key, val)
        val = _getter(key)
    return val


def _getEmptyTechScore():
    techList = getTechList()
    val = {}
    for tech in techList:
        val[tech] = dict()
        val[tech]["n"] = 0
        val[tech]["value"] = 0
    pprint(val, "New genearted empy tech score")
    return val


def _getKey(course, professor):
    return str(course) + "_" + str(professor)


def getProfCourseScore(course, professor):
    global r
    key = _getKey(course, professor)
    val = _getter(key)
    return val


def pprint(x, message=None):
    logging.debug("-" * 10)
    logging.debug(message)
    logging.debug("Type:%s" % type(x))
    logging.debug("Val:'%s'" % x)
    logging.debug("-" * 10)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # print getProfCourseScore("CMPE123", "ProfA")
    # key = "CMPE123_ProfA"
    r.delete("CMPE123_ProfA")
    # _updateTechScore(course="CMPE123",
    #                  professor="ProfA",
    #                  newTechScore={"docker": 0})
    pprint(getProfCourseScore("CMPE123", "ProfA"), "should be empty tech list")
    pprint(updateTechScore("CMPE123", "ProfA", {"docker": 0.6}), "1st")
    pprint(updateTechScore("CMPE123", "ProfA", {"docker": 0.4}), "2nd")
    pprint(updateTechScore("CMPE123", "ProfA", {"flask": 0.9}), "2nd")
