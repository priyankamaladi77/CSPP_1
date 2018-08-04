'''Guess My Number Exercise'''

def main():
    ''' guessing '''
    #s = raw_input()
    #your code here
    mid = 50
    high = 100
    low = 0
    inp = 'l'
    while inp != 'c':
        print(mid)
        inp = input("Enter 'h' if guess is too high,'l' if its too low.\
            'c' to indicate I guessed correctly")
        if inp == 'h':
            high = mid
            mid = (high + low) // 2
        elif inp == 'l':
            low = mid
            mid = (high + low) // 2
    print('your guess number is :', mid)
if __name__ == "__main__":
    main()
