import sys
import json

def main():
	tweet_file = open(sys.argv[1])

	#---- parsing txt file into json object ------

	my_output = []
	with tweet_file as f:
	    for line in f:
	        my_output.append(json.loads(line))

	#---- separating the text message from other fields

	text_list = []
	for tweet in my_output:
		if 'text' in tweet:
			text_list.append(tweet['text'])
		
	#---- spliting the words inside the tweets and summing

	count_dict = {}
	freq_dict = {}
	total_count = 0

	for text in text_list:
		words = text.split(" ")

		# summing sentiment of tweet
		for word in words:
			if word in count_dict:
				count_dict[word] = int(count_dict[word]) + 1
			else:
				count_dict[word] = 1
			total_count = total_count + 1


	# new dict with new sentiment words
	for index, word in enumerate(count_dict):
		freq_dict[word] = float(count_dict[word])/float(total_count)
		# I ignored unicode errors and characters
		try:
			print word , freq_dict[word]
		except UnicodeEncodeError:
			pass

if __name__ == '__main__':
    main()
