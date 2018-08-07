'''powerite'''
# Exercise: PowerIter
# Write a Python function, iterPower(base, exp),
# that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def iterpower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    res = 1
    for _ in range(exp):
        res = base * res
    return res





def main():
    '''powerite'''

    data = input()
    data = data.split()
    print(iterpower(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
