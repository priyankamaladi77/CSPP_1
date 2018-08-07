'''digits'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits,
#that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(number):
    '''digits'''
    # Your code here
    if number == 0:
        return number
    return number%10 +(sumofdigits(number//10))

def main():
    '''digits'''
    res = input()
    print(sumofdigits(int(res)))

if __name__ == "__main__":
    main()
