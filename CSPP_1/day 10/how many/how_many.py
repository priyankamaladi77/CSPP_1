'''how'''
#Exercise : how many
# write a procedure, called how_many,
# which returns the sum of the number of values associated
#with a dictionary.


def how_many(animals):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    ans = 0
    res = animals.values()
    for index in res:
        ans += len(index)
    return ans



def main():
    '''how'''
    num = input()
    animals = {}
    for _ in range(int(num)):
        s_i = input()
        l_i = s_i.split()
        if l_i[0][0] not in animals:
            animals[l_i[0][0]] = [l_i[1]]
        else:
            animals[l_i[0][0]].append(l_i[1])
    print(animals)
    print(how_many(animals))
if __name__ == "__main__":
    main()
