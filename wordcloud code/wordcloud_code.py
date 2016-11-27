import os
from wordcloud import WordCloud
import json


# Read the json file

f = open('samplejsonfile.json').read()

data_dict = json.loads(f)


tech_dict = data_dict["technology"]

wordString = ""

for items in tech_dict:
	for count in range(items["count"]):
            wordString += " " + (items["name"])

 
# Generate a word cloud image

wordcloud = WordCloud().generate(wordString)

image = wordcloud.to_image()

# to show the generated images
#image.show()

# to save the generated wordcloud image

wordcloud.to_file("wcImage.png")


