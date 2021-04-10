"""
File: hangman.py
Name: Ching-Ching Chuang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7
# This constant controls the wall high.
HIGH = 5


def main():
    """
    Ask user to guess the words by inputting one character in each round.
    If the input character is correct, update the words on console.
    The game will be end up with N_TURNS ran out or user get the right answer.
    """
    answer = random_word()
    guess(answer)


def guess(ans):
    turns_left = N_TURNS
    dash_cnt = len(ans)
    ini_word = ini_word_to_show(ans)
    # current word is the word to show on console in each turn
    cur_word = ini_word
    # ask for user input until it's already N guesses or it's the right answer
    while not turns_left * dash_cnt == 0:
        print('The word looks like: ', end='')
        print(cur_word)
        print('You have ' + str(turns_left) + ' guesses left.')
        input_ch = input('Your guess: ').upper()
        while not judge_if_legal(input_ch):
            print('illegal format.')
            input_ch = input('Your guess: ').upper()

        if input_ch in ans:
            print('You are correct!')
            # the input character is correct and haven't been guessed yet
            if input_ch not in cur_word:
                for i in range(len(ans)):
                    if input_ch == ans[i]:
                        dash_cnt -= 1
        else:
            print('There is no ' + input_ch + '\'s in the word.')
            turns_left -= 1
        # update the word that displayed on console
        cur_word = word_to_show(input_ch, ans, cur_word)
        draw(turns_left)

    if turns_left == 0:
        print('You are completely hung : (')
        print('The word was: ' + ans)
    elif dash_cnt == 0:
        print('You win!!')
        print('The word was: ' + ans)


def judge_if_legal(s):
    """
    :param s: str
    :return: True or False
    """
    if s.isalpha():
        if len(s) == 1:
            return True
    else:
        return False


def word_to_show(input_ch, ans, cur_word):
    """
    :param input_ch: str, an alphabet
    :param ans:str, a word
    :param cur_word: str, the word displayed on the screen
    :return: str, the updated word that will be displayed on the screen
    """
    rslt = ''
    for i in range(len(ans)):
        if input_ch == ans[i]:
            rslt += input_ch
        else:
            rslt += cur_word[i]
    return rslt


def ini_word_to_show(ans):
    """
    :param ans: str
    :return: str
    """
    ini_word = ''
    for i in range(len(ans)):
        ini_word += '-'
    return ini_word


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def draw(turns_left):
    if turns_left == N_TURNS:
        frame()
    elif turns_left == N_TURNS-1:
        one()
    elif turns_left == N_TURNS - 2:
        two()
    elif turns_left == N_TURNS - 3:
        three()
    elif turns_left == N_TURNS-4:
        four()
    elif turns_left == N_TURNS - 5:
        five()
    elif turns_left == N_TURNS - 6:
        six()
    elif turns_left == N_TURNS - 7:
        seven()


def ceiling():
    for i in range(3):
        print(' ', end='')
    for i in range(8):
        print('-', end='')
    print('')


def floor():
    for i in range(16):
        print('-', end='')
    print('')


def frame():
    ceiling()
    for i in range(HIGH):
        print('   |')
    floor()


def one():
    ceiling()
    hair()
    for i in range(HIGH - 1):
        print('   |')
    floor()


def hair():
    print('   |   |')


def head():
    print('   | ◉Ｏ◉')


def left_hand():
    print('   |  /|')


def right_hand():
    print('   |  /|\\')


def left_leg():
    print('   |  /')


def right_leg():
    print('   |  / \\')


def two():
    ceiling()
    hair()
    head()
    for i in range(HIGH - 2):
        print('   |')
    floor()


def three():
    ceiling()
    hair()
    head()
    hair()
    for i in range(HIGH - 3):
        print('   |')
    floor()


def four():
    ceiling()
    hair()
    head()
    left_hand()
    for i in range(HIGH - 3):
        print('   |')
    floor()


def five():
    ceiling()
    hair()
    head()
    right_hand()
    for i in range(HIGH - 3):
        print('   |')
    floor()


def six():
    ceiling()
    hair()
    head()
    right_hand()
    left_leg()
    for i in range(HIGH - 4):
        print('   |')
    floor()


def seven():
    ceiling()
    hair()
    head()
    right_hand()
    right_leg()
    for i in range(HIGH - 4):
        print('   |')
    floor()

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
