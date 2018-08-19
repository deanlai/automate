# Opens all text files in a directory and
# outputs any matching user supplied regular expressions
# Usage: rsearch.py /path/to/directory
# Output: <match 1>
#         <match 2>
#         <match 3>
#         ...

import os, re, sys
#change current working directory and get file names
os.chdir(sys.argv[1])
files = os.listdir(os.getcwd())
print(files)

#get regex
print('Please provide a regular expression: ')
userRegex = input()

#define search regex
searchRegex = re.compile(userRegex, re.IGNORECASE)
matches = []

#check each file for matches
for textfile in files:
    if textfile[-3:] == 'txt':
        currentFile = open(textfile)
        matches += searchRegex.findall(currentFile.read())

for match in matches:
    print(match)
