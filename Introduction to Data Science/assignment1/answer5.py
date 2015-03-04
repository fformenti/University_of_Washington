import sys
import json
import state_bounds

#---- creating a dictionary --------

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

#---- parsing txt file into json object ------

my_output = []
with open('output.txt') as f:
    for line in f:
        my_output.append(json.loads(line))

#---- separating the text message from other fields

#text_list = []
main_list = []
for tweet in my_output:
	if 'text' in tweet:
		main_list.append((tweet['text'], tweet['coordinates']))

#---- splitting the words inside the tweet and summing

state_score = {}
score_list = []
total_score = 0
for tweet in main_list:
	text = tweet[0]
	coordinates = tweet[1]
	try:
		lat_lon = coordinates['coordinates']
		latitude = lat_lon[0]
		longitude = lat_lon[1]
	except:
		#continue
		latitude = 0
		longitude = 0

	state = state_bounds.findstate(latitude,longitude)
	words = text.split(" ")
	for word in words:
		if word in scores:
			value = scores[word]
		else:
			value = 0
		total_score = total_score + value
		
		if state in state_score:
			state_score[state] = state_score[state] + total_score
		else:
			state_score[state] = total_score

	total_score = 0

max_score = -999
answer = 'no tweets from US geoposition'
for state in state_score:
	if state_score[state] > max_score and state != 'rest of the world':
		max_score = state_score[state]
		answer = state#, float(state_score[state])

print answer

