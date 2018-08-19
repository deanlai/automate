tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# check for longest word


def longestWord(table):
    longest = 0
    for i in table:
        for k in i:
            if len(k) > longest:
                longest = len(k)
    return longest


colWidth = longestWord(tableData)


def displayTable(tableData):
    numCols = len(tableData)
    numRows = len(tableData[0])
    tableString = ''
    for row in range(numRows):
        for col in range(numCols):
            tableString += tableData[col][row].rjust(colWidth + 1)
        tableString += '\n'
    print(tableString)


displayTable(tableData)
