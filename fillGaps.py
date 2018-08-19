#! /usr/bin/env python3
# fillGaps.py - finds all files of a given prefix in a single folder,
# finds gaps in numbering, and renames files to close the gap.

def fillGaps(prefix, folder):
    import os, re, shutil

    # ensures user folder destination is an absolute path.
    folder = os.path.abspath(folder)

    # create a sorted list of file numbers with correct prefix
    # at the given folder destination.
    files = os.listdir(folder)

    addDigits = (len(max(files, key=len)) - len(prefix))
    fileNumRegex = re.compile(r'^(' + prefix + r')(\d+)(\.[a-zA-Z0-9]+)$')
    sortedFileNums = []
    matchedFileNames = []
    sortedFileSufs = []
    k = 0

    # separates information from file names into lists and moves digits to front for sorting.
    for file in files:
        if re.match(fileNumRegex, file) != None:
            sortedFileNums.append(re.match(fileNumRegex, file).group(2))
            matchedFileNames.append(sortedFileNums[k].rjust(addDigits, '0') + re.match(fileNumRegex, file).group(0))
            sortedFileSufs.append(re.match(fileNumRegex, file).group(3))
            k += 1

    sortedFileNums.sort()
    matchedFileNames.sort()
    j = 0

    # removes digits used for sorting from file names.
    for file in matchedFileNames:
        matchedFileNames[j] = file[addDigits:]
        j += 1
    startNum = int(sortedFileNums[0])
    lenNum = len(sortedFileNums[-1])

    # new list populated with the correct file numbers.
    newFileNums = []
    for i in range(len(sortedFileNums)):
        newNum = str(startNum + i).rjust(lenNum, '0')
        newFileNums.append(newNum)

    i = 0

    # tests each file name to find gaps in numbering.
    for file in matchedFileNames:
        if i > 0 and file != (prefix + newFileNums[i] + sortedFileSufs[i]):
            print(file + ' ——> ' + prefix + newFileNums[i] + sortedFileSufs[i])
        else:
            print(file + ' will remain unchanged.')
        i += 1

# test run
fillGaps('ILikeCanut', '/Users/seanlai/Projects/automate/filestoorder')
