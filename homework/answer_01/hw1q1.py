print('Enter a number:')
x = input()

try:
    x = float(x)
    if x % 2 ==0 and x>=0:
        print(str(int(x))+' is a positive even number.')
    elif x % 2 == 1 and x>=0:
        print(str(int(x))+' is a positive odd number.')
    else:
        print(str(x)+' is either negative or non-integer.')
except ValueError:
    print(x +' is not a number')
