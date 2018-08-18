
stop = ["is", "a", "be"]
sentence = ["Raju", "is", "a", "be", "random"]
temp_sentence = sentence[:]
for word in temp_sentence:
	if word in stop:
		sentence.remove(word)
print(sentence)