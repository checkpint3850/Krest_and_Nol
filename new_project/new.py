game = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

for_win = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [6, 7, 8]]

print("Добро пожаловать!")

def table_game():
    print("-" * 13)

    print("|", game[0], end = " | ")
    print(game[1], end = " | ")
    print(game[2], "|")

    print("-" * 13)

    print("|", game[3], end=" | ")
    print(game[4], end=" | ")
    print(game[5], "|")

    print("-" * 13)

    print("|", game[6], end=" | ")
    print(game[7], end=" | ")
    print(game[8], "|")

    print("-" * 13)

def go(hod, XorO):
    ind = game.index(hod)
    game[ind] = XorO

def result():
    win = ""

    for i in for_win:
        if game[i[0]] == "x" and game[i[1]] == "x" and game[i[2]] == "x":
            win = "x"
        if game[i[0]] == "o" and game[i[1]] == "o" and game[i[2]] == "o":
            win = "o"
    return win

ingame = True
player_1 = True

while ingame:
    table_game()
    if player_1 == True:
        XorO = "x"
        hod = int(input("Игрок №1 введите номер ячейки -->"))
    else:
        XorO = "o"
        hod = int(input("Игрок №2 введите номер ячейки -->"))

    go(hod, XorO)
    win = result()

    if win != "":
        ingame = False
    else:
        ingame = True

    player_1 = not(player_1)

table_game()
print("Победитель ==>", win, "<==")