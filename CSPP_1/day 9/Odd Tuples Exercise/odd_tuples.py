'''odd'''
#Exercise : Odd Tuples
#Write a python function oddTuples(aTup)
# that takes a some numbers in the tuple as input and
# returns a tuple in which contains odd index values in the input tuple



def oddtuples(val):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    # val = ('I', 'am', 'a', 'test', 'tuples')
    ans = ()
    for i in range(0, len(val), 2):
        ans += (val[i], )
    return ans


def main():
    '''odd'''
    data = input()
    data = data.split()
    val = ()
    for j in enumerate(data):
        val += ((data[j]),)
    print(oddtuples(val))


if __name__ == "__main__":
    main()
