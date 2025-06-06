def matrixMult(A,B):
    return A

#matrix looks like [[a11,a21,...],[a12,a22,...],...]. [first row, second row, etc]
#matrix mult looks like (AB)11 = a11 b11 + a12b21 + a13b31+...

#check rows and columns of matrix


def validMatrix(A): #check whether each column has same length
    colNum = len(A)
    rowNum = len(A[0])
    for i in range(0,len(A)):
        if not len(A[i]) == rowNum:
            return False
    return True


def columns(A):
    if not validMatrix(A):
        return 'Not a valid matrix'
    return len(A)


def rows(A):
    if not validMatrix(A):
        return 'Not a valid matrix'
    return len(A[0])


def square(A):
    if not validMatrix(A):
        print('Not a valid matrix')
        return False
    if rows(A) == columns(A):
        return True
    return False


def matrixMult(A,B):
    if not square(A) or not square(B):
        return 'at least one non-square matrix (or invalid matrix)'
    n = rows(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    print(C)
    s = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]


    return C


A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[2,5,7],[2,2,2],[111,222,333]]
print(matrixMult(A,B))