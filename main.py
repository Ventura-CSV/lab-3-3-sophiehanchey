def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    
    #determine the maximum number through if-else statements
    maxnum = num1
    if(num2>maxnum):
        maxnum = num2
    elif(num3>maxnum):
        maxnum = num3
    else:
        maxnum

    print(f'The greatest number is {maxnum}')
    ########################################
    # Do not delete the return statement
    ########################################
    return maxnum


if __name__ == '__main__':
    main()
