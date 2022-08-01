import sympy as sp
import numpy as np

x = sp.var('x')
y = sp.var('y')
z = sp.var('z')

def eigen_vector(A,l):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=A-Z
    J=H.nullspace()
    return J
    
def eigen_value(A):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=A-Z
    DET=H.det()
    L=sp.solve(DET,x)
    l=[]
    for i in L:
        k=eigen_vector(A,i)
        for j in range(len(k)):
            l.append(k[j].tolist()) 
    M=np.empty((A.shape[0],len(l)))
    for i in range(len(l)):
        for j in range(A.shape[0]):
            M[j][i]=l[i][j][0]
    N=np.linalg.inv(M)
    K=N.dot(A)
    K=K.dot(M)
    print("\nSymmetric matrix after diagonlisation is:")
    return (K.astype(int))
    
def main():    
    n = int(input("Enter the number of variables:"))
    expr = sp.sympify(input("Enter the quadratic form:"))
    symmetric_matrix = [[] for  i in  range(n)]
    if n == 2:
        symmetric_matrix[0].append(expr.coeff(x**2))
        symmetric_matrix[0].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[1].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[1].append(expr.coeff(y**2))
        print("\nSymmetric matrix for given quadratic form is:",symmetric_matrix)
        SYMMETRIC=sp.Matrix(symmetric_matrix)
        diag=eigen_value(SYMMETRIC)
        print(diag)
        print("\nCanonical form for given quadratic form is:")
        print("{}*x**2+{}*y**2".format(diag[0,0],diag[1,1]))
    if n == 3:
        symmetric_matrix[0].append(expr.coeff(x**2))
        symmetric_matrix[0].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[0].append(int(0.5*(expr.coeff(x*z))))
        symmetric_matrix[1].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[1].append(expr.coeff(y**2))
        symmetric_matrix[1].append(int(0.5*(expr.coeff(y*z))))
        symmetric_matrix[2].append(int(0.5*(expr.coeff(x*z))))
        symmetric_matrix[2].append(int(0.5*(expr.coeff(y*z))))
        symmetric_matrix[2].append(expr.coeff(z**2))
        print("\nSymmetric matrix for given quadratic form is:",symmetric_matrix)
        SYMMETRIC=sp.Matrix(symmetric_matrix)
        eigen_value(SYMMETRIC)
        diag=eigen_value(SYMMETRIC)
        print(diag)
        print("\nCanonical form for given quadratic form is:")
        print("{}*x**2+{}*y**2+{}*z**2".format(diag[0,0],diag[1,1],diag[2,2]))
        
main()
