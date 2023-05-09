def matrix_multiply(A,B):
    C = [[0]*len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A)):
                C[i][j]= C[i][j]+A[i][k]*B[k][j]
    return C
def add_matrix(A,B):
    D = [[0]*len(B[0]) for i in range(len(A))] 
    for i in range(len(A)):
        for j in range(len(A[0])):
            D [i][j]+=A[i][j]+B[i][j]
    return D
m = int(input('Enter number of rows in matrixA '))
n = int(input('Enter number of columns in matrixA '))
A = [[0]*n for i in range(m)]
b = []
c = []

print('Enter elements in list A in column-form')
for i in range(m*n):
    b.append((int(input())))

for i in range(0,len(b),m):
    c.append(b[i:i+m])
print(c)
A = add_matrix(A,c)
for i in A:
    print(i)
B = [[]]
n = int( input('Enter a positive non-zero integer as power for above formed matrix'))
e = [[]]
if n == 1:
    B = A
elif n>1:
    B = A
    e = matrix_multiply(A,A)
    for i in range (2,n+1):
        if i ==2:
            e = matrix_multiply(A,A)
        else:
            e = matrix_multiply(e,A)
        B = add_matrix(B,e)
for i in B:
        print(i)

