'''newton'''# Write a python program to find the square root of the number
# using Newton-Rapson method

def main():
    '''newton'''
    #s = raw_input()
    #your code here
    val = int(input())
    epsilon = 0.01
    ans = val/2.0
    count = 0
    while abs(ans*ans - val) >= epsilon:
        count += 1
        ans = ans - (((ans**2) - val)/ (2*ans))
    print(str(ans))

if __name__ == "__main__":
    main()
