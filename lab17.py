import func

matrix1 = [[2.2, 1, 0.5, 2],
           [1, 1.3, 2, 1],
           [0.5, 2, 0.5, 1.6],
           [2, 1, 1.6, 2]]

matrix2 = [[2.2, 1, 0.5, 2],
           [1, 1.3, 2, 1],
           [0.5, 2, 0.5, 1.6],
           [2, 1, 1.6, 2]]

for i in matrix1:
    print(i)

E = 0.001

number = len(matrix1)
func.rotation(matrix1, matrix2, number, E)
