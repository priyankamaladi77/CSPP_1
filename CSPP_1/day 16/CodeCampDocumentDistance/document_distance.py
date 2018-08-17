'''
    Document Distance - A detailed description is given in the PDF
'''
import collections
import math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    import string
    char = string.ascii_letters + ' '
    dict1 = ''.join(index for index in dict1 if index in char)
    dict2 = ''.join(index for index in dict2 if index in char)
    dict1 = dict1.lower().strip().split()
    dict2 = dict2.lower().strip().split()

    dict3 = load_stopwords("stopwords.txt")
    for word in list(dict1):
    	if word in dict3:
    		dict1.remove(word)
    for word in list(dict2):
    	if word in dict3:
    		dict2.remove(word)

    freq1 = collections.Counter(dict1)
    freq2 = collections.Counter(dict2)


    dict4 = []
    dict5 = []
    dict6 = []
    for word in freq1:
    	if word in freq2:
    		dict4.append(freq1[word]*freq2[word])

    for word in freq1:
    	dict5.append(freq1[word]**2)

    for word in freq2:
    	dict6.append(freq2[word]**2)

    return sum(dict4)/(math.sqrt(sum(dict5))*math.sqrt(sum(dict6)))



def load_stopwords(stopwords):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwordsa = []
    with open(stopwords, 'r') as words:
        for line in words:
            stopwordsa.append(line.strip())
    return stopwordsa

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
