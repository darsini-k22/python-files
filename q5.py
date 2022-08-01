
import numpy as np

def eigenvector(x):
    return abs(x)/min(abs(x))
def releigh(a,x):
    x=abs(x)/min(abs(x))
    ax=np.dot(a,x)
    num=np.dot(ax,x)
    den=np.dot(x,x)
    return num/den

n = int(input('Enter order of matrix: '))


a = np.zeros((n,n))


print('Enter Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

x = np.zeros((n))

print('Enter initial guess vector: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))

tolerable_error = float(input('Enter tolerable error: '))

max_iteration = int(input('Enter maximum number of steps: '))

condition =  True
step = 1
while condition==True:
    t=x
    x=np.dot(a,x)
    
    dif=sum(eigenvector(x))-sum(eigenvector(t))
    condition= step<max_iteration and abs(dif)>tolerable_error
    step+=1
    
print(eigenvector(x))
print('eigen value',releigh(a,eigenvector(x)))