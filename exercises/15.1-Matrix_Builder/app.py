import random

#Create the function below:



def matrixBuilder(n):

    matrix = []

    for i in range(n):

        row = []

        for j in range(n):

            row.append(1)

        matrix.append(row)

    return matrix

print(matrixBuilder(5))
    
