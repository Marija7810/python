import os

os.system("cls")


class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def create_board(self):
        b = self.cells = [" "] * 9
        return b

    def display(self, b):
        print("%s| %s | %s" % (self.cells[0], self.cells[1], self.cells[2]))
        print("--------")
        print("%s| %s | %s" % (self.cells[3], self.cells[4], self.cells[5]))
        print("--------")
        print("%s| %s | %s" % (self.cells[6], self.cells[7], self.cells[8]))
        b = self.cells
        return 0

    def update_cell(self, cell_number, player, b):

        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player
            b = self.cells
        else:
            print("Zauzeto polje. Izaberite drugo")
            choice = int(input("\n " + player + ") Odaberi ponovo 1-9. >"))
            board.update_cell(choice, player)
        return b


    def who_first(self):
        who_f = input("Ko ce prvi da igra? (X/O) >").upper()
        if who_f == "X":
            player = "X"
            #board.game(player)
        elif who_f == "O":
            player = "O"
            #board.game(player)
        else:
            print("Greska, unesite ponovo")
            board.who_first()
        return player

    def is_winner(self, player, b):
        if b[0] == player and b[1] == player and b[2] == player:
            return True
        elif b[3] == player and b[4] == player and b[5] == player:
            return True
        elif b[6] == player and b[7] == player and b[8] == player:
            return True
        elif b[0] == player and b[3] == player and b[6] == player:
            return True
        elif b[1] == player and b[4] == player and b[7] == player:
            return True
        elif b[2] == player and b[5] == player and b[8] == player:
            return True
        elif b[0] == player and b[4] == player and b[8] == player:
            return True
        elif b[2] == player and b[4] == player and b[6] == player:
            return True
        else:
            return False

    def is_tie(self, b):
        used = 0
        for cell in b:
            if cell != " ":
                used += 1
        if used == 9:
            return True
        else:
            return False

    def play_again(self):
        pl_again = input("Da li zelite ponovo da igrate? (Y/N) >").upper()
        if pl_again == "Y":
            return pl_again
        elif pl_again == "N":
            return pl_again
        else:
            print("Unesi ponovo")
            Board.play_again(self)

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

    """def game(self, player):
        board = Board()
        while True:
            choice = board.input(player)
            board.update_cell(choice, player, b)
            refresh()

            if board.is_winner(player):
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
        return player
"""
    def refresh(self, b):
        os.system('cls')
        Board.print_header(self)
        Board.display(self, b)


    def print_header(self):
        print("XOXO\n")

board = Board()
#board.who_first()
