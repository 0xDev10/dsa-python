# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

test = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]

max_col = len(test[0])
max_row = len(test)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(test[y][x])
        rows[y].append(test[y][x])
        fdiag[x+y].append(test[y][x])
        bdiag[x-y-min_bdiag].append(test[y][x])

print(cols)
print(rows)
print(fdiag)
print(bdiag)

##########################################################################################
def print_diagonals(matrix):
    n = len(matrix)
    diagonals_1 = []  # lower-left-to-upper-right diagonals
    diagonals_2 = []  # upper-left-to-lower-right diagonals
    for p in range(2*n-1):
        diagonals_1.append([matrix[p-q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
        diagonals_2.append([matrix[n-p+q-1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)])
    print("lower-left-to-upper-right diagonals: ", diagonals_1)
    print("upper-left-to-lower-right diagonals: ", diagonals_2)


print_diagonals([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5],
])