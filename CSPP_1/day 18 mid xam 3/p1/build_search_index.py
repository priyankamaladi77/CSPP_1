'''
	Tiny Search Engine - Part 1 - Build a search index

	In this programming assingment you are given with some text documents as input.
	Complete the program below to build a search index. Don't worry, it is explained below.
	A search index is a python dictionary.
	The keys of this dictionary are words contained in ALL the input text documents.
	The values are a list of documents such that the key/word appears in each document atleast once.
	The document in the list is represented as a tuple.
	The tuple has 2 items. The first item is the document ID.
	Document ID is represented by the list index.
	For example: the document ID of the third document in the list is 2
	The second item of the tuple is the frequency of the word occuring in the document.

	Here is the sample format of the dictionary.
	{
		word1: [(doc_id, frequency),(doc_id, frequency),...],
		word2: [(doc_id, frequency),(doc_id, frequency),...],
		.
		.
	}
'''
# helper function to load the stop words from a file
def load_stopwords(stopwords):
	'''
		loads stop words from a file and returns a dictionary
	'''
	stopwords1 = {}
	with open(stopwords, 'r') as f_stopwords:
		for line in f_stopwords:
			stopwords1[line.strip()] = 0
	return stopwords1


def word_list(text):
	'''
		Change case to lower and split the words using a SPACE
		Clean up the text by remvoing all the non alphabet characters
		return a list of words
	'''
	import string

	list1 = []
	text1 = text.lower().split(' ')
	characters = string.ascii_letters + ' '
	text1 = ''.join(index for index in text1 if index in characters)
	list1 = list1.append(text1)
	text2 = load_stopwords("stopwords.txt")
	for word in list(text1):
		if word in text2:
			list1.append(text1.remove(word))
	return list1


def build_search_index(docs):
	'''
		Process the docs step by step as given below
	'''

	# initialize a search index (an empty dictionary)

	# iterate through all the docs
	# keep track of doc_id which is the list index corresponding the document
	# hint: use enumerate to obtain the list index in the for loop

		# clean up doc and tokenize to words list

		# add or update the words of the doc to the search index

	# return search index
	search_index = {}
	for index in docs:
		for index in enumerate(docs):
			docs[index] += list_index
	word_list = doc.clear().word_tokenize(text)
	search_index = search_index.update(word_list)
	return search_index


# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
	'''
		print the search index
	'''
	keys = sorted(index.keys())
	for key in keys:
		print(key, " - ", index[key])

# main function that loads the docs from files
def main():
	'''
		main function
	'''
	# empty document list
	documents = []
	# iterate for n times
	lines = int(input())
	# iterate through N times and add documents to the list
	for i in range(lines):
		documents.append(input())
		i += 1

	# call print to display the search index
	print_search_index(build_search_index(documents))

if __name__ == '__main__':
	main()
