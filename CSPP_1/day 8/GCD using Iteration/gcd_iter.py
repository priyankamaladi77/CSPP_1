'''gcditer'''
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b),
# that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcditer(ans1, ans2):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    for i in range(1, ans1+1):
        if ans1%i == 0 and ans2%i == 0:
            gcd = i
    return gcd





def main():
    '''gcditer'''
    data = input()
    data = data.split()
    print(gcditer(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
