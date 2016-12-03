# task: from a given review, for a list of keywords find the sentiment
import json
import requests
import urllib
import os
import logging
import copy

techListFile = os.path.join(os.path.dirname(__file__), "tech_list.json")
with open(techListFile) as fp:
    _techList = json.load(fp)
_techList = [str(x).lower() for x in _techList]

logging.getLogger('requests.packages.urllib3').setLevel(logging.ERROR)


def _getSentiment(line):
    line = str(line)
    # TODO move all the credentials and url info to config file
    payload = {'outputMode': 'json',
               'text': line,
               "apikey": "e32e49b4c38bd84accea2cf1f72c32cf9e633c7f"}
    payload = urllib.urlencode(payload)
    payload.encode('ascii')
    url = 'http://access.alchemyapi.com/calls/text/TextGetTextSentiment'
    url = '%s?%s' % (url, payload)  # TODO there must be a better way ;P
    r = requests.get(url)
    docSentiment = json.loads(r.content)["docSentiment"]
    if docSentiment["type"] == "neutral":
        return None
    else:
        return float(docSentiment["score"])


def getTechScore(review, techList=None):
    # TODO use logging
    # print "#" * 80
    # print " " * 35 + "START"
    # print "#" * 80
    # print review
    if techList is None:
        techList = _techList
    review = review.replace("!", ".")
    reviewLines = review.split(".")
    reviewLines = [line.strip() for line in reviewLines]
    reviewLines = [line.lower() for line in reviewLines]

    techScoreList = {}
    for tech in techList:
        techScoreList[tech] = []

    for line in reviewLines:
        for tech in techList:
            if tech in line:
                sentiment = _getSentiment(line)
                # print tech, line, sentiment
                if sentiment:
                    techScoreList[tech].append(sentiment)
    # print techScoreList
    techScore = {}
    for tech in techScoreList:
        if len(techScoreList[tech]):
            techScore[tech] = sum(techScoreList[tech]) / len(
                techScoreList[tech])
    # print techScore
    # print "#" * 80
    # print " " * 35 + "END"
    # print "#" * 80
    return techScore


def getTechList():
    return copy.deepcopy(_techList)


if __name__ == "__main__":
    review = """Prof taught us docker very well. Flask was not good though.
            He skipped Django. Flask was good then."""
    print getTechScore(review)
