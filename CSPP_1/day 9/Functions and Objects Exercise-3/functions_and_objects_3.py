'''obj3'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts
# the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(list1):
    '''obj3'''
    return list1 * list1

def apply_to_each(list1, func):
    '''obj3'''
    ans = map(square, list1)
    return list(ans)



def main():
    '''obj3'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
