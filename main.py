import sudoku as su
import solver as so
import time
import itertools
import threading
import sys

done_solving = False

def loading_animation():
    for c in itertools.cycle(['.  ', '.. ', '...', '   ']):
        if done_solving:
            break
        sys.stdout.write('\rSolving Sudoku' + c)
        sys.stdout.flush()
        time.sleep(0.5)

digits = [
    0, 0, 5, 0, 4, 0, 8, 0, 0,
    0, 3, 0, 2, 0, 0, 0, 6, 0,
    0, 0, 0, 5, 0, 3, 9, 0, 0,
    0, 6, 9, 0, 0, 0, 0, 0, 0,
    0, 4, 2, 0, 0, 0, 6, 9, 0,
    0, 0, 0, 0, 0, 0, 1, 3, 0,
    0, 0, 7, 6, 0, 2, 0, 0, 0,
    0, 8, 0, 0, 0, 7, 0, 5, 0,
    0, 0, 3, 0, 8, 0, 4, 0, 0
          ]

# digits = [
#     5, 0, 0, 9, 0, 4, 0, 7, 0,
#     0, 0, 0, 0, 0, 7, 0, 0, 0,
#     0, 2, 0, 0, 1, 0, 0, 0, 0,
#     9, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 6, 1, 0, 2, 0,
#     0, 8, 5, 4, 0, 0, 0, 0, 0,
#     4, 0, 0, 8, 0, 2, 0, 5, 0,
#     0, 0, 0, 7, 0, 0, 3, 9, 6,
#     0, 0, 0, 0, 0, 0, 0, 0, 0
#           ]

# digits = [
#     3, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 1, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 6, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0
#           ]

sudoku = su.Sudoku(digits)
sudoku.print_field()

solver = so.Solver(sudoku)

# start the loading animation
print()
t = threading.Thread(target=loading_animation)
t.start()

start_t = time.time()
solver.solve()
end_t = time.time()

# stop the loading animation
done_solving = True

print()
print()
solver.sudoku.print_field()
print("Runtime: " + str(round(end_t - start_t, 2)) + "s")