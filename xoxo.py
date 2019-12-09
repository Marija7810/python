import os

os.system("cls")


class Board:

    def __init__(self):
        self.cells = [" "] * 9

    def display(self):

        print("%s| %s | %s" % (self.cells[0], self.cells[1], self.cells[2]))
        print("--------")
        print("%s| %s | %s" % (self.cells[3], self.cells[4], self.cells[5]))
        print("--------")
        print("%s| %s | %s" % (self.cells[6], self.cells[7], self.cells[8]))

    def update_cell(self, cell_number, player):

        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player
        else:
            print("Zauzeto polje. Izaberite drugo")
            choice = int(input("\n " + player + ") Odaberi ponovo 0-8. >"))
            board.update_cell(choice, player)

    @staticmethod
    def who_first():
        who_f = input("Ko ce prvi da igra? (X/O) >").upper()
        if who_f == "X":
            board.game(who_f)
        elif who_f == "O":
            board.game(who_f)
        else:
            print("Pogresan unos! Moze samo x ili o. Unesite ponovo")
            board.who_first()

    def input(self, player):
        t1 = True
        while t1:
            try:
                choice = int(input("\n" + player + ") Odaberi 0-8. >"))
                if choice < 0 or choice > 8:
                    continue
            except ValueError:
                continue
            t1 = False
        return choice

    def again(self):

        play_again = input("Da li zelite ponovo da igrate? (Y/N) >").upper()
        if play_again == "Y":
            return play_again
        elif play_again == "N":
            return play_again
        else:
            print("Unesi ponovo")
            board.again()

    def game(self, player):
        while True:

            choice = board.input(player)
            board.update_cell(choice, player)
            refresh()

            if board.winner(player):
                print("\n" + player + " je pobednik!\n")
                play_again = board.again()
                if play_again == "Y":
                    board.__init__()
                    board.who_first()
                    continue
                elif play_again == "N":
                    break

            if board.is_tie():
                print("\nNereseno!\n")
                play_again = board.again()
                if play_again == "Y":
                    board.__init__()
                    board.who_first()
                    continue
                elif play_again == "N":
                    break

            if player == "X":
                player = "O"
            else:
                player = "X"



    def winner(self, player):
        if self.cells[0] == player and self.cells[1] == player and self.cells[2] == player:
            return True
        elif self.cells[3] == player and self.cells[4] == player and self.cells[5] == player:
            return True
        elif self.cells[6] == player and self.cells[7] == player and self.cells[8] == player:
            return True
        elif self.cells[0] == player and self.cells[3] == player and self.cells[6] == player:
            return True
        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        elif self.cells[0] == player and self.cells[4] == player and self.cells[8] == player:
            return True
        elif self.cells[2] == player and self.cells[4] == player and self.cells[6] == player:
            return True
        else:
            return False

    def is_tie(self):
        used = 0
        for cell in self.cells:
            if cell != " ":
                used += 1
        if used == 9:
            return True
        else:
            return False
    # def reset_board(self):
    #   self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]


board = Board()

def print_header():
    print("XOXO\n")

def refresh():
    os.system('cls')
    print_header()
    board.display()

board.who_first()
