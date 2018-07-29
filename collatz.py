def collatz(number):
    if number%2 == 0:
        print(number/2)
        return number/2
    else:
        print(number*3 + 1)
        return(number*3 + 1)

while True:
    try:
        intInput = int(input('Please enter an integer: '))
        break
    except ValueError:
        print('That is not an integer!')
while intInput != 1:
    intInput = collatz(intInput)
