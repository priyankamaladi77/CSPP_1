'''bisection'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''bisection'''
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    #step = 0.1
    # your code starts here
    val = int(input())
    low = 0.0
    high = val
    ans = (high + low)/2.0
    while abs(ans**2 - val) >= epsilon:
        if ans**2 < val:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print(ans)
if __name__ == "__main__":
    main()
