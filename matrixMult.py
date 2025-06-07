def matrixMult(A, B):
    return A


# matrix looks like [[a11,a21,...],[a12,a22,...],...]. [first row, second row, etc]
# matrix mult looks like (AB)11 = a11 b11 + a12b21 + a13b31+...

# check rows and columns of matrix


def validMatrix(A):  # check whether each column has same length
    colNum = len(A)
    rowNum = len(A[0])
    for i in range(0, len(A)):
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


def matrixAdd(A,B):
    #just assume they're the correct dimensions etc
    m, n = rows(A), columns(A)
    C = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrixSubtract(A,B):
    #just assume they're the correct dimensions etc
    m, n = rows(A), columns(A)
    C = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def matrixMult(A, B):
    if not rows(A) == columns(B):
        return 'rows of first must equal columns of second (or invalid matrix)'
    n = rows(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    s = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


'''def strassen(A, B):  # fast matrix multiplication, assumes square matrices
    #not finished, need to pad out matrices to be of dimension 2^n
    
    
    if not square(A) or not square(B):
        return 'matrices must be square'

    if not rows(A) == rows(B):
        return 'matrices must be same size'

    n = rows(A)

    if n <= 2:
        return matrixMult(A, B)

    m = n // 2

    A11, B11 = [row[:m] for row in A[:m]], [row[:m] for row in B[:m]]
    A12, B12 = [row[m:] for row in A[:m]], [row[m:] for row in B[:m]]
    A21, B21 = [row[:m] for row in A[m:]], [row[:m] for row in B[m:]]
    A22, B22 = [row[m:] for row in A[m:]], [row[m:] for row in B[m:]]

    M1 = strassen(A11, matrixSubtract(B12, B22))
    M2 = strassen(matrixAdd(A11, A12), B22)
    M3 = strassen(matrixAdd(A21, A22), B11)
    M4 = strassen(A22, matrixSubtract(B21, B11))
    M5 = strassen(matrixAdd(A11, A22), matrixAdd(B11, B22))
    M6 = strassen(matrixSubtract(A12, A22), matrixAdd(B21, B22))
    M7 = strassen(matrixSubtract(A11, A21, matrixAdd(B11, B12)))

    # define C = A * B, C = [[C11, C12],[C21,C22]]
    C11 = matrixSubtract(matrixAdd(M5,M4), matrixAdd(M2,M6))
    C12 = matrixAdd(M1, M2)
    C21 = matrixAdd(M3, M4)
    C22 = matrixSubtract(matrixAdd(M5, M1), matrixSubtract(M3, M7))

    return [[C11, C12], [C21, C22]]'''


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 5, 7], [2, 2, 2], [111, 222, 333]]

print(matrixAdd(A,B))