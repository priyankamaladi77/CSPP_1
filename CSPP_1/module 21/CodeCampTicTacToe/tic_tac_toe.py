def looping(seti):
	if 'x' in seti:
		return 'x'
	return 'o'

def game_play(game):

	set1 = set()
	set2 = set()
	set3 = set()
	set4 = set()
	set5 = set()
	length = len(game)
	for i in range(length):
		for j in range(len(game[i])):
			if i == j:
				set1.add(game[i][j])
			if i + j == (len(game)-1):
				set2.add(game[i][j])
			sett = set(game[i])
			if len(sett) == 1:
				if 'x' in sett:
					return 'x'
				return 'o'
			if j == 0:
				set3.add(game[i][j])
			if j == 1:
				set4.add(game[i][j])
			if j == 2:
				set5.add(game[i][j])
	if len(set1) == 1:
		return looping(set1)
	if len(set2) == 1:
		return looping(set2)
	if len(set3) == 1:
		return looping(set3)
	if len(set4) == 1:
		return looping(set4)
	if len(set5) == 1:
		return looping(set5)
	return "draw"

def validity_check(game):
	x_element = 'x'
	o_element = 'o'
	xcount = 0
	ocount = 0
	countt = 0
	for index in game:
		if len(index) != 3:
			return "invalid game"
		if x_element in index:
			xcount += index.count(x_element)
		if o_element in index:
			ocount += index.count(o_element)
		if '.' in index:
			countt += index.count('.')
	if xcount+ocount+countt != 9:
		return "invalid input"
	if abs(xcount - ocount) != 1:
		return "invalid game" 
	return game_play(game)

def main():
	row = []
	for _ in range(3):
		column = input()
		column = list(map(str, column.split(' ')))
		row.append(column)
	row = validity_check(row)
	print(row)
if __name__ == '__main__':
	main()
