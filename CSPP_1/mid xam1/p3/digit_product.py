'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    sum1 = 1
    while int_input > 0:
        rem = int_input%10
        sum1 = sum1*rem
        int_input = int_input//10
    print(sum1)


if __name__ == "__main__":
    main()
