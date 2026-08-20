import os

def majority(ls):
	max = 1
	for x in ls:
		i = ls.count(x)
		if i > max:
			max = i
	return max

if __name__ == "__main__":
	ls = [12, 3, 2, 2, 2, 1, 1, 1, 4, 4, 4, 4]
	print(majority(ls))

