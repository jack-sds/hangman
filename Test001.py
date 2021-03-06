import math
import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_______       ",
              "|             ",
              "|      |      ",
              "|      〇     ",
              "|      |      ",
              "|      /＼    ",
              "              "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    
    while wrong < len(stages) - 1:
        print("\n")
        char = input("一文字を予想しろ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたのWIN")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け正解は{}.".format(word))


words = ["cat","avarage","sora","yesterday","combine","conclude","cloud","kafka"]

hangman(random.choice(words))