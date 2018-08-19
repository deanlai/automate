#!/usr/bin/env python3
# gapFiller.py - finds files with a matching prefix (e.g. spam001.txt, spam002.txt),
# locates gaps in the numbering, and renames subsequent files to shift into the gaps.
# Usage - $python3 gapFiller.py path/to/folder

# needed modules
import re
import os
import sys
import shutil

# create regex to find filenames with matching prefix
prefixRegex = re.compile(r'''
    ^(\D*)?   #matches anything before numbers
    (\d+)     #matches numbers
    (\.\w+)$  #matches extension
    ''', re.VERBOSE)

# create absolute path to folder and populate a list with all filenames
folder = os.path.abspath(sys.argv[1])
fileList = os.listdir(folder)
fileList.sort()

# initialize data
fileDict = {}
numDigits = 0

# Function for creating number strings (e.g. '2' --> '002')


def createNums(digits, int):
    return (digits - len(str(int)))*'0' + str(int)


# populate dictionary of file lists with file extensions as keys. Only populates for files matching prefixRegex.
# e.g. {'.txt': ['bar001.txt, foo2.txt'], '.py': ['eggs42.py, spam99.py']}
for file in fileList:
    mo = prefixRegex.search(file)
    if mo != None:
        if fileDict.get(mo.group(3)) == None:
            fileDict.setdefault(mo.group(3), [mo.group(0)])
        else:
            fileDict[mo.group(3)].append(mo.group(0))

for key in fileDict:                            # loop through keys (file extensions)
    incrementCounter = 0
    lastPrefix = ''
    # loop through list of files in each key (file extension)
    for file in fileDict[key]:

        mo = prefixRegex.search(file)           # create regex match object for file
        currentPrefix = mo.group(1)             # set current prefix

        if currentPrefix != lastPrefix:         # check to see if current prefix matches last,
            incrementCounter = 0                # otherwise reset increment counter
            numDigits = len(mo.group(2))        # and reset digit string length

        # check if filename number is greater than current increment (maybe always true?)
        if int(mo.group(2)) > incrementCounter:
            incrementCounter += 1               # Increment by 1

            # Rename file with correct shifted increment using shutil.move()
            newFile = mo.group(1) + createNums(numDigits, incrementCounter) + mo.group(3)
            print('Renaming "%s" to "%s"...' % (file, newFile))
            shutil.move(os.path.join(folder, file), os.path.join(folder, newFile))
            lastPrefix = currentPrefix
