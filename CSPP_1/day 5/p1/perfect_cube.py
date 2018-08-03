'''perfect cube'''# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    '''perfect cube'''
    # input is captured in s
    #s = raw_input()
    # watch out for the data type of value stored in s
    # your code starts here
    cube = int(input())
    ans = 0
    while ans**3 < cube:
        ans += 1
    if ans**3 != cube:
        print(cube,"is not a perfect cube")
    else:
        print(cube,"is a perfect cube")

if __name__ == "__main__":
    main()
