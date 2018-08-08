'''obj2'''
#Exercise : Function and Objects Exercise-2
#Implement a function that converts
# the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def increment(list1):
    '''obj2'''
    return list1+1


def apply_to_each(list1, func):
    '''obj2'''
    ans = map(increment, list1)
    return list(ans)



def main():
    '''obj2'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, increment))

if __name__ == "__main__":
    main()
