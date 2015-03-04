import sys
import json

#---- creating a dictionary --------

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

#---- parsing txt file into json object ------

my_output = []
with open('problem_1_submission.txt') as f:
    for line in f:
        my_output.append(json.loads(line))

#---- separating the text message from other fields

text_list = []
for tweet in my_output:
	if 'text' in tweet:
		text_list.append(tweet['text'])
	
#---- spliting the words inside the tweet and summing

new_dict = {}
total_dict = {}
new_terms = []

for text in text_list:
	words = text.split(" ")

	# summing sentiment of tweet
	total_score = 0
	for word in words:
		if word in scores:
			value = scores[word]
		else:
			value = 0
			new_terms.append(word)
		total_score = total_score + value

	# new dict with new sentiment words based on the total score of the tweet
	for word in new_terms:
		if word in total_dict:
			total_dict[word] = int(total_dict[word]) + total_score
		else:
			total_dict[word] = int(total_score)

# new dict with new sentiment words
for index, word in enumerate(total_dict):
	new_dict[word] = float(total_dict[word])/float(new_terms.count(word))
	# I ignored unicode errors and characters
	try:
		print word , new_dict[word]
	except UnicodeEncodeError:
		pass
