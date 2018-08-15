'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
#cardvalues = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4,
# '5':5, '6':6, '7':7, '8':8, '9':9}
def sort(hand):
    '''To sort the hand'''
    count = len(hand)
    new_hand_values = []
    for index in range(count):
        if hand[index][0] == 'T':
            new_hand_values.append(10)
        elif hand[index][0] == 'J':
            new_hand_values.append(11)
        elif hand[index][0] == 'Q':
            new_hand_values.append(12)
        elif hand[index][0] == 'K':
            new_hand_values.append(13)
        elif hand[index][0] == 'A':
            new_hand_values.append(14)
        else:
            new_hand_values.append(int(hand[index][0]))
    return new_hand_values
def is_straight(hand):
    '''To call is_straight'''
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    size = len(hand)
    #new_hand_values = []
    sort_list = sorted(sort(hand))
    for index in range(size-1):
        if sort_list[index+1] - sort_list[index] != 1:
            return False
    return True

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check
        if it is a flush
        Write the code for it and return True if it is a
        flush else return False
    '''
    size = len(hand)
    for index in range(size-1):
        if hand[index][1] != hand[index+1][1]:
            return False
    return True

def is_fourofakind(hand):
    '''To call fourkind'''
    count = 0
    sort_list = sorted(sort(hand))
    for index in range(len(sort_list)-3):
        if sort_list[index] == sort_list[index+1] == sort_list[index+2] == sort_list[index+3]:
            count += 1
        if count == 1:
            return True
        return False


def is_threeof_kind(hand):
    '''To call threeofkind'''
    count = 0
    sort_list = sorted(sort(hand))
    for index in range(len(sort_list)-2):
        if sort_list[index] == sort_list[index+1] == sort_list[index+2]:
            count += 1
        if count == 1:
            return True
        return False


def is_onepair(hand):
    '''To call is onepair'''
    sort_list = sorted(sort(hand))
    set_list = set(sort_list)
    if len(sort_list) - len(set_list) == 1:
        return True
    return False


def is_twopair(hand):
    '''To call twopair'''
    sort_list = sorted(sort(hand))
    set_list = set(sort_list)
    if len(sort_list) - len(set_list) == 2:
        return True
    return False


def is_fullhouse(hand):
    '''To call fullhouse'''
    count = 0
    index = 0
    sort_list = sorted(sort(hand))
    if sort_list[index] == sort_list[index+1] == sort_list[index+2] \
    or sort_list[index+3] == sort_list[index+4]:
        count += 1
    elif sort_list[index+3] == sort_list[index+4] and \
    sort_list[index] == sort_list[index+1] == sort_list[index+2]:
        count += 1
    if count == 1:
        return True
    return False


def hand_rank(hand):

    '''
    You will code this function. The goal of the function is to
    return a value that max can use to identify the best hand.
    As this function is complex we will progressively develop it.
    The first version should identify if the given hand is a straight
    or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    '''
    '''
    if is_threeof_kind(hand):
        return 3
    if is_onepair(hand):
        return 1
    if is_twopair(hand):
        return 2
    if is_fullhouse(hand):
        return 7
    if is_fourofakind(hand):
        return 4
    if is_straight(hand) and is_flush(hand):
        return 8
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    return 0


    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = (line.split(" "))
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
