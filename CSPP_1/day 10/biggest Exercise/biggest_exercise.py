'''Exercise : Biggest Exercise'''
#Write a procedure, called biggest, which returns the key
#corresponding to the entry with the largest
#number of values associated
#with it.If there is more than one such entry,
#return any one of the matching keys.


def biggest(a_dict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest
    #number of values associated with it
    '''
    # Your Code Here
    result = 0
    max_str = ""
    for i_1 in a_dict:
        if len(a_dict[i_1]) > result:
            result = len(a_dict[i_1])
            max_str += i_1
    return max_str[-1]
def main():
    '''main'''
    num = input()
    a_dict = {}
    for _ in range(int(num)):
        s_i = input()
        l_i = s_i.split()
        if l_i[0][0] not in a_dict:
            a_dict[l_i[0][0]] = [l_i[1]]
        else:
            a_dict[l_i[0][0]].append(l_i[1])
    print(biggest(a_dict))
if __name__ == "__main__":
    main()
