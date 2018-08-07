'''gcdrecr'''
# Exercise: GCDRecr
# Write a Python function, gcdrecur(a, b),
# that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdrecur(ans1, ans2):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if ans2 == 0:
        return ans1
    else:
        return gcdrecur(ans2, ans1%ans2)




def main():
    '''gcdrecr'''
    data = input()
    data = data.split()
    print(gcdrecur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
