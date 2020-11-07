import numpy as np
import matplotlib.pyplot as plt


# O(n) Mathod:

def Fibonacci_Matrix_Calc (i):
    
    # Define an intitial list to store the result.
    F_list = [0, 1]
    
    # Define matrix operator.
    Matrix_Op = np.matrix('1 1; 1 0', dtype = np.longlong)
    # Define initial vector (1, 0).
    Matrix_0 = np.matrix('1; 0', dtype = np.longlong)
    
    # Matrix operation.
    for n in range (1, i-1):
        Matrix_N = Matrix_Op * Matrix_0
        Matrix_0 = Matrix_N
        
        # Insert the number into the list.
        Matrix_to_Array = np.array(Matrix_N).ravel()
        F_list.append(Matrix_to_Array[0])

    return (F_list)

#Driver:
F = Fibonacci_Matrix_Calc(10)
print (F)
#Notice: Numpy matrix defalt data type is int32... so after the 47th number it will overflow...

# Plot:
F_plot_val = Fibonacci_Matrix_Calc(93)
# x axis
def axis_x():
    list_axis_x = []
    l = 0
    for l in range (1, len(F_plot_val)+1):
        list_axis_x.append(l)
        l += l
    return (list_axis_x)
a_x = axis_x()
plt.plot(a_x, F_plot_val, 'o')
plt.show()


# O(logn) Mathod:

# Define the "A" Matrix.
A = [[1, 1], [1, 0]]

# Difine Initial Vector.
V = [1, 0]

# Matrices miltiplication (the matrices are expected in the form of a list of 2x2 size).
def Multiply_Matrices(Matrix_1, Matrix_2):
    # Calc Matrix x Vector.
    if np.ndim(Matrix_2) == 1:
        New_Metrix_c1_r1 = Matrix_1[0][0] * Matrix_2[0] + Matrix_1[0][1] * Matrix_2[1]
        New_Metrix_c1_r2 = Matrix_1[0][0] * Matrix_2[0] + Matrix_1[0][1] * Matrix_2[1]
        New_Vector = [New_Metrix_c1_r1, New_Metrix_c1_r2]
        return New_Vector
    # Calc Matrix x Matrix.        
    New_Metrix_c1_r1 = Matrix_1[0][0] * Matrix_2[0][0] + Matrix_1[0][1] * Matrix_2[1][0]
    New_Metrix_c1_r2 = Matrix_1[0][0] * Matrix_2[0][1] + Matrix_1[0][1] * Matrix_2[1][1]
    New_Metrix_c2_r1 = Matrix_1[1][0] * Matrix_2[0][0] + Matrix_1[1][1] * Matrix_2[1][0]
    New_Metrix_c2_r2 = Matrix_1[1][0] * Matrix_2[0][1] + Matrix_1[1][1] * Matrix_2[1][1]
    # Calc Result.
    New_Metrix = [[New_Metrix_c1_r1, New_Metrix_c1_r2], [New_Metrix_c2_r1, New_Metrix_c2_r2]]
    return New_Metrix

# Matrix Exponentiation Calc.
def Matrix_Exponentiation(M, p):
    if p == 1:
        return M
    elif p % 2 == 0:
        return Matrix_Exponentiation(Multiply_Matrices(M, M), p//2)
    else:
        # If devided by 2 remain 1, then need to multiply with "A" one more time.
        return Multiply_Matrices(M, Matrix_Exponentiation(Multiply_Matrices(M, M), p//2))

# Output the Nth Fibonacci Number.
Nth_Fib = 21
print(Multiply_Matrices((Matrix_Exponentiation(A, Nth_Fib - 1)), V)[0])


# O(1) Time Complexcity..

# Nth Fibonacci Number.
N = 21

# Golden Ratio Phi.
phi = (1 + np.sqrt(5))/2
#Conjugate of Golden Ratio Phi.
phi_con = (1 - np.sqrt(5))/2

# Initial Vector.
V = np.matrix('1, 0')

# Eigenbasis S and S-Inverse Matrices.
S_mtx = np.matrix([[phi, 1], [phi_con, 1]])
S_inv = (1/np.sqrt(5)) * np.matrix([[1, -1], [-phi_con, phi]])

# A Matrix and A^n Matrix.
A_mtx = np.matrix([[phi, 0],[0, phi_con]])
A_to_the_n_mtx = np.matrix([[phi ** (N-1), 0], [0, phi_con ** (N-1)]])

# Calc [Fn, Fn-1] = S x A^n x S^-1 x V
Fn_Fn_m1 = V * S_inv * A_to_the_n_mtx * S_mtx
FN = np.array(Fn_Fn_m1).ravel()

print (FN[0])





# Create Fibonacci Numbers Function

def Fibonacci_calc(i):

    # Innitializing first 2 numbers (basic cases) in the Fibonacci number set.
    Fn_group = [1, 1]

    # Case 1: only one number.
    if i == 1:
        return (Fn_group.pop(Fn_group[-1]))

    # Case 2: only 2 numbers.
    if i == 2:
        return (Fn_group)

    # Calc and return the required Fibonacci number array.
    for x in range (1, i):
        Fn_group.append(Fn_group[-1] + Fn_group[-2])
    return (Fn_group)

print(Fibonacci_calc(21)
