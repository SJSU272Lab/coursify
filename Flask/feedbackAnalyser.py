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
    if techScore:
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


def getCourseScore(course):
    keys = _keys("%s_*" % course)
    score = {}
    for key in keys:
        tempscore = _getter(key)
        # Duplication of code
        # TODO make a functionto accept two tech scores and and add them
        for tech in tempscore:
            tempTotal = tempscore[tech]['value'] * tempscore[tech]['n']
            tempN = tempscore[tech]['n']
            if tech in score:
                presentTotal = score[tech].get('value', 0) * score[tech].get(
                    'n', 0)
                # pprint(tempTotal, "tempTotal")
                tempN += score[tech].get('n', 0)
                tempTotal += presentTotal
            else:
                score[tech] = {}
            if tempN:
                score[tech]['value'] = tempTotal / tempN
                score[tech]['n'] = tempN
            else:
                score[tech]['value'] = 0
                score[tech]['n'] = 0
    return score


def pprint(x, message=None):
    logging.debug("-" * 10)
    logging.debug(message)
    logging.debug("Type:%s" % type(x))
    logging.debug("Val:'%s'" % x)
    logging.debug("-" * 10)


def _keys(pattern="*"):
    return r.keys(pattern)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # print getProfCourseScore("CMPE123", "ProfA")
    # key = "CMPE123_ProfA"

    for key in r.keys("CMPE272*"):
        r.delete(key)
    # _updateTechScore(course="CMPE272",
    #                  professor="ProfA",
    #                  newTechScore={"docker": 0})
    pprint(getProfCourseScore("CMPE272", "ProfA"), "should be empty tech list")
    pprint(updateTechScore("CMPE272", "ProfA", {"docker": 0.6,
                                                "flask": 0.4}), "1st")
    pprint(updateTechScore("CMPE272", "ProfB", {"docker": 0.4,
                                                "elastic": 0.8}), "2nd")
    pprint(getCourseScore("CMPE272"))
    # pprint(updateTechScore("CMPE272", "ProfA", {"flask": 0.9}), "2nd")
