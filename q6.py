import numpy as np
def func(a,x):
    for i in range(10):
        x = np.dot(a, x)
        x_n = x / x.min()
    print('Eigen vector of matrix {} using Power method is {}'.format(a.tolist(), x_n))
    find_ray(a,x_n)
    print("\n")
    
def find_ray(a,x_n):
    h=np.dot(a,x_n)
    m=np.dot(h,x_n)
    
    x_2=np.dot(x_n,x_n)
    dom_eival=m/x_2
    print('The dominant eigen value for matrix {}  using Reyleigh quotient is {:.2f}'.format(a.tolist(),dom_eival))
    
ab = np.array([[2, -12],[1, -5]]) 
a=np.array([[2,1],[0,-4]])  
x=np.array([1,1]) 
b=np.array([[-5,0,0],[3,7,0],[4,-2,3]])
c=np.array([[1,2,-2],[-2,5,-2],[-6,6,-3]])
x1=np.array([1,1,1])
func(ab,x)
func(a,x)
func(b,x1)
func(c,x1)
