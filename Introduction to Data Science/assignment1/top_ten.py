import sys
import json
from collections import Counter
import operator

def main():
	tweet_file = open(sys.argv[1])

	#---- parsing txt file into json object ------

	my_output = []
	with tweet_file as f:
	    for line in f:
	        my_output.append(json.loads(line))

	#---- separating the hashtags message from other fields an append them all in a list

	hashtags_list = []
	for tweet in my_output:
		if 'entities' in tweet:
			entities = tweet['entities']
			hashtags = entities['hashtags']
			for hashtag in hashtags:
				if hashtag:
					contents = hashtag['text']
					hashtags_list.append(contents)
		
	#---- counting the occurrences of each element inside the list, and creating a dict from it
	hashtags_count = Counter(hashtags_list)

	#----- sorting dict by values and making it a list
	sorted_hastags = sorted(hashtags_count.items(), key=operator.itemgetter(1), reverse=True)

	i = 0
	while (i < 10):
		answer = sorted_hastags[i]
		#try:
		print answer[0] , float(answer[1])
		i = i + 1
		#except UnicodeEncodeError:
		#	pass

if __name__ == '__main__':
    main()
