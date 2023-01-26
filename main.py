def game():
    dictionary = {"A1": " ",
                  "B1": " ",
                  "C1": " ",
                  "A2": " ",
                  "B2": " ",
                  "C2": " ",
                  "A3": " ",
                  "B3": " ",
                  "C3": " "
                  }

    continue_game = True
    turn = 0
    while continue_game:
        if turn % 2 == 0:
            symbol = 'X'
        else:
            symbol = 'O'

        C = str(input(f"Player {symbol}, it is your turn, please write the coordinate: ").upper())

        right_place = False
        while not right_place:
            if C in dictionary.keys():
                for key in dictionary:
                    if C == key:
                        if dictionary[key] == ' ':
                            dictionary[key] = symbol
                            right_place = True
                            break
                        else:
                            C = input("There is already a symbol here, please write another coordinate: ")
            else:
                C = input("This is not a valid coordinate. Write another one: ")

        print("           A  B  C\n"
              f"       1 {dictionary['A1']} | {dictionary['B1']} | {dictionary['C1']}  \n"
              f"        -----------\n"
              f"       2 {dictionary['A2']} | {dictionary['B2']} | {dictionary['C2']}  \n"
              f"        -----------\n"
              f"       3 {dictionary['A3']} | {dictionary['B3']} | {dictionary['C3']}  \n")


        if dictionary['A1'] == dictionary['B1'] == dictionary['C1'] and dictionary['C1'] != ' ' or\
            dictionary['A2'] == dictionary['B2'] == dictionary['C2'] and dictionary['C2'] != ' ' or\
            dictionary['A3'] == dictionary['B3'] == dictionary['C3'] and dictionary['C3'] != ' ' or\
            dictionary['A1'] == dictionary['A2'] == dictionary['A3'] and dictionary['A3'] != ' ' or\
            dictionary['B1'] == dictionary['B2'] == dictionary['B3'] and dictionary['B3'] != ' ' or\
            dictionary['C1'] == dictionary['C2'] == dictionary['C3'] and dictionary['C3'] != ' ' or\
            dictionary['C3'] == dictionary['B2'] == dictionary['A1'] and dictionary['A1'] != ' ' or\
            dictionary['A3'] == dictionary['B2'] == dictionary['C1'] and dictionary['C1'] != ' ':

            print(f"Player {symbol} won. Congratulations!")
            continue_game = False

        if ' ' not in dictionary.values():
            print("That is a DRAW!")
            continue_game = False
        turn += 1

print("Welcome to the Tic-Tac-Toe Game\n"
      "First, some explanations:\n"
      "The game will be played using a coordinate system, where the columns are letters and the rows are numbers.\n"
      "Example:  A  B  C\n"
      "       1   |   |  \n"
      "        -----------\n"
      "       2 X |   |  \n"
      "        -----------\n"
      "       3   |   |  \n"
      "The X's coordinate is A2.\n")

A = input("Let's play? Y/N\n")

while A == 'Y':
    game()
    A = input("Would you like to play again? Y/N ")
else:
    print("Bye!")

