import xoxo3
import os
import pytest


class Test:

    def test_create_board(self):
        b = xoxo3.Board()
        d = b.create_board()
        assert d == [" "] * 9

    def test_display(self):
        b = xoxo3.Board()
        d = b.__init__()
        c = b.create_board()
        assert b.display(c) is 0

    def test_update_cell(self):
        b = xoxo3.Board()
        player = "x"
        c = b.create_board()
        xoxo3.input = lambda choice: "3"
        assert b.update_cell(3, player, c) == [" ", " ", " ", "x", " ", " ", " ", " ", " "]

    def test_who_first(self):
        b = xoxo3.Board()
        who_f = "X"
        xoxo3.input = lambda who_f: "X"
        assert b.who_first() == "X"


    @pytest.mark.parametrize('par_board',
                             [
                                 (["x", "x", "x", " ", " ", " ", " ", " ", " "]),
                                 (["x", " ", " ", "x", " ", " ", "x", " ", " "]),
                                 (["x", " ", " ", " ", "x", " ", " ", " ", "x"])

                             ])

    def test_winner(self, par_board):
        b = xoxo3.Board()
        assert b.winner('x', par_board)

    @pytest.mark.parametrize('par_board1',
                             [
                                 (["x", "x", "x", "o", "o", "o", "x", "x", "o"]),
                                 (["x", "o", "x", "x", "o", "x", "x", "o", "o"]),
                                 (["x", "o", "x", "o", "x", "x", "o", "x", "x"])

                             ])
    def test_is_tie(self, par_board1):
        b = xoxo3.Board()
        assert b.is_tie(par_board1)

    def test_play_again(self):
        b = xoxo3.Board()
        xoxo3.input = lambda pl_again: "Y"
        assert b.play_again() == "Y"


    def test_input(self):
        b = xoxo3.Board()
        player = "X"
        xoxo3.input = lambda choice: "3"
        assert b.input(player) == 3