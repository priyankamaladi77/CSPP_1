'''factorial'''
# Exercise: Assignment-1
# Write a Python function, factorial(n),
# that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(ans):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if ans == 0:
        return 1
    return ans * factorial(ans-1)



def main():
    '''factorial'''
    val = input()
    print(factorial(int(val)))

if __name__ == "__main__":
    main()
