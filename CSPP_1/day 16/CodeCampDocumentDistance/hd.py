for word in load_stopwords:
    	if word in dict1:
        	print(word)
        	dict1 = dict1.replace(word,"")
        	