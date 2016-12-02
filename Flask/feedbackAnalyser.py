from recommender.techScore import getTechScore

import logging


def analyse(feedback):
    techScore = getTechScore(feedback['review'])
    logging.debug("TecScore: %s" % techScore)
    pushToElastic(feedback)


def pushToElastic(feedback):
    # TODO
    logging.info("#" * 10 + "TODO" + "#" * 10)
    logging.info("Pushing feedback to elastic")
