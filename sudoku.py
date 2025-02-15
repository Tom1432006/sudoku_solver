class Digit:
    box = 0
    row = 0
    column = 0
    value = 0

    def __init__(self, box, row, column, value):
        self.box = box
        self.row = row
        self.column = column
        self.value = value
    
    def set_val(self, val):
        self.value = val

    def compare(self, val):
        return self.value == val

class Box:
    digits = [] # a box contains 9 digits
    index = 0

    def __init__(self, index, digits=[]):
        self.digits = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
        self.index = index
        if digits != []:
            self.digits = digits
    
    def has_digit(self, val):
        for digit in self.digits:
            if digit.compare(val): return True

        return False
    
    def from_digits(self, digits):
        for i in range(len(digits)):
            self.digits[int(i / 3)][i % 3] = digits[i]
    
    def insert_digit(self, digit, r, c):
        self.digits[r % 3][c % 3] = Digit(self.index, r, c, digit)
    
    def update_digit(self, digit, r, c):
        self.digits[r % 3][c % 3].set_val(digit)
    
    def print_box(self):
        print("Box " + str(self.index) + ":", end="")
        for r in self.digits:
            print(" | ", end="")
            for c in r:
                print(str(c.value) + " ", end="")
        print("\n ----------------------------")
    
    def check(self):
        contains = []

        for r in self.digits:
            for c in r:
                if c.value not in contains and c.value != 0:
                    contains.append(c.value)
                elif c.value != 0:
                    return False
        return True
    
    def get_digits(self, ignore_null):
        for r in self.digits:
            for c in r:
                if c.value != 0 and ignore_null: yield c
    
    def get_digit(self, row, col):
        return self.digits[row][col].value

    def get_row(self, row):
        for d in self.digits[row]:
            yield d


class Sudoku:
    field = []

    def __init__(self, digits):
        self.field = [Box(i) for i in range(9)] # a Field contains 9 Boxes
        for i in range(len(digits)):
            # get the field box, the digit belongs to
            r = int(i / 9)
            c = i % 9

            box_no = int(r / 3) * 3 + int(c / 3)

            self.field[box_no].insert_digit(digits[i], r, c)

    def print_field(self):
        # go through every row
        for row in range(9):
            # go through every gox in that row
            for box in range(0, 3):
                # convert this information to a box number
                box_no = int(row / 3) * 3 + box

                # get the one specific row from the box and print it out
                for digit in self.field[box_no].get_row(row % 3):
                    print(digit.value, end="")

                # make it pretty
                if box != 2: print(" | ", end="")
            if row == 2 or row == 5:
                print("\n---------------")
            else: print()
    
    def check(self):
        # check every box
        for box in self.field:
            if box.check() == False: return False


        # check every row and column. i is for both at the same time
        for i in range(9):
            if self.check_row_and_column(i) == False: return False
                        
        return True
    
    def check_row_and_column(self, i):
        # save all the previously contained digits, to check if digits are repeating
        contains_row = []
        contains_col = []
        for box in self.field: # check every box
            for digit in box.get_digits(ignore_null=True):
                # if the box hast digits in the row i
                if digit.row == i:
                    # check if the digits has already occured in the row 
                    if digit.value not in contains_row:
                        contains_row.append(digit.value)
                    else:
                        return False
                
                # if the box has digits in the column i
                if digit.column == i:
                    # check if the digits has already occured in the column
                    if digit.value not in contains_col:
                        contains_col.append(digit.value)
                    else:
                        return False
            
        return True
    
    def insert_digit(self, digit, index):
        row = int(index / 9)
        col = index % 9

        box_no = int(row / 3) * 3 + int(col / 3)

        self.field[box_no].insert_digit(digit, row, col)
    
    def update_digit(self, digit, index):
        row = int(index / 9)
        col = index % 9

        box_no = int(row / 3) * 3 + int(col / 3)

        self.field[box_no].update_digit(digit, row, col)
    
    def get_digit(self, index):
        row = int(index / 9)
        col = index % 9

        box_no = int(row / 3) * 3 + int(col / 3)

        return self.field[box_no].get_digit(row % 3, col % 3)
