'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''newton raphson'''
    val = int(input())
    epsilon = 0.01
    ans = val/2.0
    count = 0
    while abs(ans*ans - val) >= epsilon:
        count += 1
        ans = ans - (((ans**2) - val)/ (2*ans))
    print(str(ans))
    # epsilon and step are initialized
    # don't change these values
    # your code starts here
if __name__ == "__main__":
    main()
