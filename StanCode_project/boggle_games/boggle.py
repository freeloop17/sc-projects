"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""
from datetime import datetime

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DICTIONARY_LIST = []

word_cnt = 0


def main():
	"""
	TODO:
	"""
	letter_list = get_letters()
	# letter_list = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	start_time = datetime.now()
	read_dictionary()
	find_word(letter_list)
	end_time = datetime.now()
	print("There are", word_cnt, "words in total.")
	print("time:", str(end_time-start_time))


def find_word(lst):
	for y in range(4):
		for x in range(4):
			find_word_helper(lst, x, y, '', [], [])


def find_word_helper(lst, x, y, current_word, xy_record, current_word_lst):
	global word_cnt
	if len(current_word) >= 4 and current_word not in current_word_lst:
		current_word_lst.append(current_word)
		if current_word in DICTIONARY_LIST:
			word_cnt += 1
			print("Found \"", current_word, "\"")
	else:
		# Choose
		current_word += lst[y][x]
		xy_record.append([x, y])
		# Explore
		pos_lst = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
		for dx, dy in pos_lst:
			if not has_prefix(current_word):
				break
			else:
				if 0 <= x + dx < 4 and 0 <= y + dy < 4:
					if [x + dx, y + dy] not in xy_record:
						find_word_helper(lst, x + dx, y + dy, current_word, xy_record, current_word_lst)
		# Un-choose
		xy_record.remove([x, y])


def get_letters():
	lst = []
	first_row_letters = input("1 row of letters: ")
	first_lst = first_row_letters.split(' ')
	first_lst = [x.lower() for x in first_lst if isinstance(x, str)]
	for letter in first_lst:
		if len(letter) > 1 or len(first_lst) != 4:
			print("Illegal input")
			exit()
	second_row_letters = input("2 row of letters: ")
	second_lst = second_row_letters.split(' ')
	second_lst = [x.lower() for x in second_lst if isinstance(x, str)]
	for letter in second_lst:
		if len(letter) > 1 or len(second_lst) != 4:
			print("Illegal input")
			exit()
	third_row_letters = input("3 row of letters: ")
	third_lst = third_row_letters.split(' ')
	third_lst = [x.lower() for x in third_lst if isinstance(x, str)]
	for letter in third_lst:
		if len(letter) > 1 or len(third_lst) != 4:
			print("Illegal input")
			exit()
	forth_row_letters = input("4 row of letters: ")
	forth_lst = forth_row_letters.split(' ')
	forth_lst = [x.lower() for x in forth_lst if isinstance(x, str)]
	for letter in forth_lst:
		if len(letter) > 1 or len(forth_lst) != 4:
			print("Illegal input")
			exit()
	lst.append(first_lst)
	lst.append(second_lst)
	lst.append(third_lst)
	lst.append(forth_lst)

	return lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open('dictionary.txt', 'r') as f:
		for line in f:
			DICTIONARY_LIST.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in DICTIONARY_LIST:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
