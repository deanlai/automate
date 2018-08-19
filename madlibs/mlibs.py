#mlibs.py - writes a mad lib from a template with user input
#Usage: mlibs.py <template file> <madlib file>


import re, sys

#Imports a text file
templateFile = open(sys.argv[1])
madTemplate = templateFile.read()

#Take user input function
def takeInput(wordType):
    conj = ' a '
    if wordType == 'adjective':
        conj = ' an '
    print('Enter' + conj + wordType + ':')
    return input()

#Modify text with user input
wordRegex = re.compile(r'NOUN|ADJECTIVE|VERB|ADVERB')
mo = wordRegex.search(madTemplate)
while mo != None:
    madTemplate = wordRegex.sub(takeInput(mo.group().lower()), madTemplate, count = 1)
    mo = wordRegex.search(madTemplate)

#Write user modified madlib to file
madlibFile = open(sys.argv[2], 'w')
madlibFile.write(madTemplate)
madlibFile.close()
