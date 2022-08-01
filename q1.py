import sympy as sp

def eigen_vector_calculation(A,y):
    n=A.shape[0]
    I=sp.eye(n)
    Z=I.multiply(y)
    H=A-Z
    J=H.nullspace()
    O=[]
    for i in range(len(J)):
        print("Eigen Vector for Eigen Value {} is => {}".format(y,J[i].tolist()))
        O.append(J[i].tolist())
    print(O)
    

x=sp.var('x')
# A=sp.Matrix([[4,0,1],[-2,1,0],[-2,0,1]])
A=sp.Matrix([[5,-3],[6,-4]])
row=sp.shape(A)[0]
col=sp.shape(A)[1]
x0=sp.ones(col,1)
I=sp.eye(row)
X=A-x*I
y=sp.solve(sp.det(X),x)
print('Eigen Values are:',y)

for i in y:
    eigen_vector_calculation(A, i)



