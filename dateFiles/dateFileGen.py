import os, random

def randDateGen(region):
    month = str(random.randint(1,12))
    day = str(random.randint(1,31))
    year = str(random.randint(1900,2099))
    if region == 'america':
        return month + '-' + day + '-' + year
    elif region == 'europe':
        return day + '-' + month + '-' + year

fileNum = 40

catNames = ['Eldor', 'Dorita', 'Schmetterling', 'Bhagavad']


for i in range(fileNum):
    dateFile = open('Mypet' + catNames[random.randint(0,3)] + randDateGen('america') + '.txt', 'w')
    dateFile.write('Meow '*random.randint(3,25))
    dateFile.close()
