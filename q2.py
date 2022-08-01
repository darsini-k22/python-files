import sympy as sp
import numpy as np
x=sp.var('x')

def calculate_eigen_vector(A,l):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=A-Z
    J=H.nullspace()
    return J
    
def calculate_eigen_values(A):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=A-Z
    DET=H.det()
    L=sp.solve(DET,x)
    print(L)
    l=[]
    for i in L:
        k=calculate_eigen_vector(A,i)
  
        for j in range(len(k)):
            l.append(k[j].tolist())
        # print(l)
    M=np.empty((A.shape[0],len(l)))
    # print(M)
 
    for i in range(len(l)):
        for j in range(A.shape[0]):
            M[j][i]=l[i][j][0]
            # print(l[i][j][0])
    # print(M)
    N=np.linalg.inv(M)
    K=N.dot(A)
    K=K.dot(M)
    # print("{} after diagonalizing the matrix is:\n".format(A.tolist()))
    # print(K.astype(int))
    # print("\n")
                
A=sp.Matrix([[1,0],[6,-1]])
B=sp.Matrix([[2,0,-2],[0,3,0],[0,0,3]])
C=sp.Matrix([[-1,7,-1],[0,1,0],[0,15,-2]])

calculate_eigen_values(A)
calculate_eigen_values(B)
calculate_eigen_values(C)
