#Explain your work

#Question 1
import random
primeNumbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(primeNumbers[random.randint(0,len(primeNumbers)-1)])
print(matrix,"\n")
for i in range(3):
    for j in range(3):
        print("{:2}".format(matrix[i][j]),end=" ")
    print()
