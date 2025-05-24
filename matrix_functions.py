import math 

''''
#Sample matrices
w = [[1],
     [3],
     [4],
     [9]]

x = [[1],
     [2],
     [9],
     [9]]
'''


def sigmoid(num):
    return 1/(1+ math.exp(-num)) #returns value b/w 0 and 1
                                 #for high num it tends to 1
                                 #for high negative num it tends to 0

def tranpose(matrix):
    m = len(matrix)
    n = len(matrix[0]) # to get number of elements in each row
    tmatrix = [[0 for x in range(m)]for y in range(n)] #initializes a matrix of required rows and columns with 0s
    for i in range(m):
        for j in range(n):
            tmatrix[j][i] = matrix[i][j]
    return tmatrix

def multiply(a,b):
    b = tranpose(b)
    result = [[0 for x in range(len(a))] for y in range(len(a))] # creates an empty matrix initialzed with zeroes
    
    for i in range(len(a)): #looping through each row of a
        for j in range(len(a)): #looping through each column of b
            summation = 0 
            for k in range(len(a[0])): #looping through each element of the column of b
                summation += a[i][k]*b[k][j]
            result[i][j] = summation
    return result

def dot_product(a,b):
    result = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            result += a[i][j]*b[j][i]
    return result


'''

b = -120
y_hat = sigmoid((dot_product(tranpose(w),x) + b)) #predicted y = σ(w_t⋅x + b); w_t = transpose of w

print(y_hat)
'''