'''obj1'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given
# testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(tlist, func):
    '''obj1'''
    ans = map(abs, tlist)
    return list(ans)



def main():
    '''obj1'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
