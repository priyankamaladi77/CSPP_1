'''logic for tic_tac_toe'''
def looping(seti):
    ''' looping '''
    if 'x' in seti:
        return 'x'
    return 'o'

def game_play(game):
    ''' game play function'''
    set_1 = set()
    set_2 = set()
    set_3 = set()
    set_4 = set()
    set_5 = set()
    length_1 = len(game)
    for i in range(length_1):
        for j in range(len(game[i])):
            if i == j:
                set_1.add(game[i][j])
            if i + j == (len(game)-1):
                set_2.add(game[i][j])
            set1 = set(game[i])
            if len(set1) == 1:
                if 'x' in set1:
                    return 'x'
                return 'o'
            if j == 0:
                set_3.add(game[i][j])
            if j == 1:
                set_4.add(game[i][j])
            if j == 2:
                set_5.add(game[i][j])
    if len(set_1) == 1:
        return looping(set_1)
    if len(set_2) == 1:
        return looping(set_2)
    if len(set_3) == 1:
        return looping(set_3)
    if len(set_4) == 1:
        return looping(set_4)
    if len(set_5) == 1:
        return looping(set_5)
    return "draw"

def check_for_validity(game):
    '''validation'''
    x_element = 'x'
    o_element = 'o'
    x_count = 0
    o_count = 0
    count1 = 0
    for index in game:
        if len(index) != 3:
            return "invalid game"
        if x_element in index:
            x_count += index.count(x_element)
        if o_element in index:
            o_count += index.count(o_element)
        if '.' in index:
            count1 += index.count('.')
    if x_count+o_count+count1 != 9:
        return "invalid input"
    if abs(x_count - o_count) != 1:
        return "invalid game"
    return game_play(game)

def main():
    '''main function'''
    rows = []
    for _ in range(3):
        columns = input()
        columns = list(map(str, columns.split(' ')))
        rows.append(columns)
    rows = check_for_validity(rows)
    print(rows)
if __name__ == '__main__':
    main()
