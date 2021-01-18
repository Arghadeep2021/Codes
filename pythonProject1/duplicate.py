def countletters(words):
    if words < 1:
        return 0
    else:
        return len(words[0]) + countletters(words[1:])
sentence = ['he', 'is' , 'very', 'naughty']
print(sentence)
print(countletters(sentence))