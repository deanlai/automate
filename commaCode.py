spam = ['apples', 'bananas', 'tofu', 'cats']
def printList(list):
    for i in range(len(list)-1):
        print(list[i] + ', ', end='')
    print('and ' + list[-1] +'.')

printList(spam)
spam = spam*3
printList(spam)
