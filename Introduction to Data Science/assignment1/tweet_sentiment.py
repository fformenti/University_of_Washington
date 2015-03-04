import sys
import json


def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#hw()
	#lines(sent_file)
	#lines(tweet_file)

	#---- creating a dictionary --------

	#afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

	#---- parsing txt file into json object ------

	my_output = []
	with tweet_file as f:
	    for line in f:
	    	print 'passou'
	        my_output.append(json.loads(line))

	#---- separating the text message from other fields

	text_list = []
	for tweet in my_output:
		if 'text' in tweet:
			text_list.append(tweet['text'])

	#---- spliting the words inside the tweet and summing

	score_list = []
	total_score = 0
	for text in text_list:
		words = text.split(" ")
		for word in words:
			if word in scores:
				value = scores[word]
			else:
				value = 0
			total_score = total_score + value
		score_list.append(total_score)
		print total_score
		total_score = 0
	#print score_list

if __name__ == '__main__':
	main()
