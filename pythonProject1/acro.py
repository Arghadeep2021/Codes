def first(words):
    return words[0]
def acronym(words):
    acro = ''
    acro = acro.join(list(map(first,words))).upper()
    return acro
words = ['he', 'is', 'a', 'very', 'bad', 'boy']
acro= acronym(words)
print(acro)

