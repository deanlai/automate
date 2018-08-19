def likes(names):
    noOne = 'no one'
    singular = ' likes this'
    plural = ' like this'
    if len(names) == 0:
        print(noOne + singular)
    elif len(names) == 1:
        print(names[0] + singular)
    elif len(names) == 2:
        print(names[0] + ' and ' + names[1] + plural)
    elif len(names) == 3:
        print(names[0] + ', ' + names[1] + ' and ' + names[2] + plural)
    else:
        print(names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others' + plural)
