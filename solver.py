import os

class Solver:
    sudoku = None

    starting_digits = []

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.starting_digits = [False for _ in range(81)]

        self.get_starting_digits()

    def get_starting_digits(self):
        for i in range(81):
            self.starting_digits[i] = self.sudoku.get_digit(i) != 0

    def solve(self):
        # solve the sudoku recursively
        # go through every digit and try every number, until a solution is found
        move_back = False 

        i = 0
        while i < 81:
            # do not change the starting digits
            if self.starting_digits[i]:
                if move_back: i -= 1
                else: i += 1
                continue 


            move_back = False
            # iterate through the diffrent possible digits
            curr = self.sudoku.get_digit(i)

            self.sudoku.update_digit(curr+1, i)

            if False:
                os.system('clear')
                self.sudoku.print_field()

            if self.sudoku.check() == True and curr < 9:
                i += 1
                continue
            elif curr >= 8:
                self.sudoku.update_digit(0, i)
                i -= 1
                move_back = True
            
