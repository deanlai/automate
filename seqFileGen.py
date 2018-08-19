import random


def addDigits(num):
    newNum = num + random.randint(1, 2)
    return (3-len(newNum))*'0' + str(newNum)


fileNum = 80

filePrefix = ['Spam', 'Nigiri', 'Patchai', 'Canut']
fileExt = ['.txt', '.py', '.js']

for i in range(fileNum):
    dateFile = open('ILike' + filePrefix[random.randint(0, 3)] + addDigits(i) +
                    fileExt[random.randint(0, 2)], 'w')
    dateFile.write('Meow '*random.randint(3, 25))
    dateFile.close()
