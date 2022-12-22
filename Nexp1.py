prefixes = ['de','con']
suffixes = ['er','s']

def parse(word):
    prefix = ''
    suffix = ''

    # find all prefixes
    found = True
    while found:
        found = False
        for p in prefixes:
            if word.startswith(p):
                prefix += p
                word = word[len(p):] # remove prefix from word
                found = True

    # find all suffixes
    found = True
    while found:
        found = False
        for s in suffixes:
            if word.endswith(s):
                suffix = s + suffix
                word = word[:-len(s)] # remove suffix from word
                found = True

    return (prefix, word, suffix)

print (parse('construct'))
print (parse ('destructer'))
print (parse('deconstructs'))
print (parse('deconstructers'))
print (parse('deconstructser'))
print (parse('condestructser'))
print (parse('condenses'))
