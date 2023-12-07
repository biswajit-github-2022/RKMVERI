#!/usr/bin/env python
# coding: utf-8
"""
-----------------------------------------------------------------------------
Assignment-4: Matrix computation exercise using python and numpy
-----------------------------------------------------------------------------
AUTHOR: Soumitra Samanta (soumitra.samanta@gm.rkmvu.ac.in)
-----------------------------------------------------------------------------
Package required:
Numpy: https://numpy.org/
Matplotlib: https://matplotlib.org
-----------------------------------------------------------------------------
"""

import numpy as np
from numpy.random import RandomState

from typing import Tuple

__all__ = [
    'vector_dot_product',
    'matrix_multiplication',
    'elementary_ops_interchange_rows',
    'elementary_ops_scale_row',
    'elementary_ops_change_row',
    'elementary_ops_interchange_rows_mult',
    'elementary_ops_scale_row_mult',
    'elementary_ops_change_row_mult',
    'elementary_ops_interchange_cols',
    'elementary_ops_scale_col',
    'elementary_ops_change_col',
    'elementary_ops_interchange_cols_mult',
    'elementary_ops_scale_col_mult',
    'elementary_ops_change_col_mult',
    'sweep_out_row',
    'sweep_out_row_mult',
    'sweep_out_col',
    'sweep_out_col_mult',
    'reduced_echelon_form',
    'reduced_upper_triangular_form',
    'reduce_non_sigular_matrix_to_identity',
    'generate_random_linear_system',
    'soln_n_equations_n_unknowns',
    'reduce_to_hcf_matrix',
    'soln_m_equations_n_unknowns',
    'determinant_matrix',
    'soln_n_equations_n_unknowns_cramers_rule',
    'factorize_to_lu_matrix',
    'soln_n_equations_n_unknowns_lu_factorization',
    
    
]


def vector_dot_product(
    x: np.array,
    y: np.array,
)->float:
    """
    Dot product between two vectors
    
    Inputs:
        - x: 1st vector
        - y: 2nd vector
       
    Output:
        - val: Dot product between x and y
    
    """
    
    val = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    sum=0
    for i in range(len(y)):
        sum=sum+x[i]*y[i]
        sum1=np.dot(x,y)
        if sum==sum1:
            print("function is correct")
            val=sum
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
    
    return val


def matrix_multiplication(
    x: np.array,
    y: np.array,
)->np.array:
    """
    Dot product between two vectors
    
    Inputs:
        - x: 1st matrix
        - y: 2nd matrix
       
    Output:
        - val: multiplication x and y
    
    """
    
    val = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    for i in range(len(x)):
        val1=[]
        for j in range(len(y[0])):
            sum=0
            for k in range(len(y)):
                sum=sum+x[i][k]*y[k][j]
            val1.append(sum)
        val.append(val1)
    val=np.array(val)

    
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
    
    return val


def elementary_ops_interchange_rows(
    A: np.array, 
    ith_row: int, 
    jth_row: int
)->np.array:
    """
    Elementary row operation: interchange i-th and j-th rows
    
     Inputs:
        - A: Given matrix
        - ith_row: i-th row
        - jth_row: j-th row
        
    Output:
        - A: Resultant rows interchhanged matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#

    for k in range(len(A[0])):
        temp=A[ith_row][k]
        A[ith_row][k]=A[jth_row][k]
        A[jth_row][k]=temp
    
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def elementary_ops_scale_row(
    A: np.array, 
    ith_row: int, 
    scalar_val: float
)->np.array:
    """
    Elementary row operation: Scaling i-th row  with the scalar_val value
    
     Inputs:
        - A: Given matrix
        - ith_row: row want to scale
        - scalar_val: scalar value
        
    Output:
        - A: Resultant row scaling matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    for j in range(len(A[0])):
        if A[ith_row-1][j] != 0:
            A[ith_row-1][j]*=scalar_val
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def elementary_ops_change_row(
    A: np.array, 
    ith_row: int, 
    jth_row: int,
    scalar_val: float
)->np.array:
    """
    Elementary row operation: Change i-th based on i<-i + scalar_val*j
    
     Inputs:
        - A: Given matrix
        - ith_row: i-th row
        - jth_row: j-th row
        - scalar_val: scalar value
        
    Output:
        - A: Resultant row updated matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    B = elementary_ops_scale_row(A.copy(), jth_row, scalar_val)
    for k in range(len(A[0])):
        A[ith_row-1][k]+=B[jth_row-1][k] 
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def elementary_ops_interchange_rows_mult(
    A: np.array, 
    ith_row: int, 
    jth_row: int
)->Tuple[np.array, np.array]:
    """
    Elementary row operation: interchange i-th and j-th rows
    
     Inputs:
        - A: Given matrix
        - ith_row: i-th row
        - jth_row: j-th row
        
    Output:
        - A: Resultant rows interchhanged matrix
    """
    
    I = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    I= np.eye(len(A))
    I = elementary_ops_interchange_rows(I, ith_row, jth_row)
    A = matrix_multiplication(I, A)
    
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, I


def elementary_ops_scale_row_mult(
    A: np.array, 
    ith_row: int, 
    scalar_val: float
)->Tuple[np.array, np.array]:
    """
    Elementary row operation: Scaling i-th row  with the scalar_val value
    
     Inputs:
        - A: Given matrix
        - ith_row: row want to scale
        - scalar_val: scalar value
        
    Output:
        - A: Resultant row scaling matrix
    """
    
    I = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    I= np.eye(len(A))
    I = elementary_ops_scale_row(I, ith_row, scalar_val)
    A = matrix_multiplication(I, A)
    
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, I


def elementary_ops_change_row_mult(
    A: np.array, 
    ith_row: int, 
    jth_row: int,
    scalar_val: float
)->Tuple[np.array, np.array]:
    """
    Elementary row operation: Change i-th based on i<-i + scalar_val*j
    
     Inputs:
        - A: Given matrix
        - ith_row: i-th row
        - jth_row: j-th row
        - scalar_val: scalar value
        
    Output:
        - A: Resultant row updated matrix
    """
    
    I = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#

    I = np.eye(len(A))
    I = elementary_ops_change_row(I, ith_row, jth_row, scalar_val)
    A = matrix_multiplication(I, A)
    
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, I


def elementary_ops_interchange_cols(
    A: np.array, 
    ith_col: int, 
    jth_col: int
)->np.array:
    """
    Elementary col operation: interchange i-th and j-th cols
    
     Inputs:
        - A: Given matrix
        - ith_col: i-th col
        - jth_col: j-th col
        
    Output:
        - A: Resultant cols interchhanged matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#

    for k in range(len(A)):
        temp=A[k][ith_col-1]
        A[k][ith_col-1]=A[k][jth_col-1]
        A[k][jth_col-1]=temp
    
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def elementary_ops_scale_col(
    A: np.array, 
    ith_col: int, 
    scalar_val: float
)->np.array:
    """
    Elementary col operation: Scaling i-th col  with the scalar_val value
    
     Inputs:
        - A: Given matrix
        - ith_col: col want to scale
        - scalar_val: scalar value
        
    Output:
        - A: Resultant col scaling matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    for j in range(len(A)):
        A[j][ith_col-1]*=scalar_val
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def elementary_ops_change_col(
    A: np.array, 
    ith_col: int, 
    jth_col: int,
    scalar_val: float
)->np.array:
    """
    Elementary col operation: Change i-th col based on i<-i + scalar_val*j
    
     Inputs:
        - A: Given matrix
        - ith_col: i-th col
        - jth_col: j-th col
        - scalar_val: scalar value
        
    Output:
        - A: Resultant col updated matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    B = elementary_ops_scale_col(np.copy(A), jth_col, scalar_val)
    for k in range(len(A)):
        A[k][ith_col-1]+=B[k][jth_col-1]
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def elementary_ops_interchange_cols_mult(
    A: np.array, 
    ith_col: int, 
    jth_col: int
)->np.array:
    """
    Elementary col operation: interchange i-th and j-th cols
    
     Inputs:
        - A: Given matrix
        - ith_col: i-th col
        - jth_col: j-th col
        
    Output:
        - A: Resultant cols interchhanged matrix
    """
    
    I = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    I = np.eye(len(A[0]))
    I = elementary_ops_interchange_rows(I, ith_col, jth_col)
    A = matrix_multiplication(A, I)
    
    
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, I


def elementary_ops_scale_col_mult(
    A: np.array, 
    ith_col: int, 
    scalar_val: float
)->Tuple[np.array, np.array]:
    """
    Elementary col operation: Scaling i-th col  with the scalar_val value
    
     Inputs:
        - A: Given matrix
        - ith_col: col want to scale
        - scalar_val: scalar value
        
    Output:
        - A: Resultant col scaling matrix
    """
    
    I = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    I = np.eye(len(A[0]))
    I = elementary_ops_scale_row(I, ith_col, scalar_val)
    A = matrix_multiplication(A, I)
    
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, I


def elementary_ops_change_col_mult(
    A: np.array, 
    ith_col: int, 
    jth_col: int,
    scalar_val: float
)->Tuple[np.array, np.array]:
    """
    Elementary col operation: Change i-th col based on i<-i + scalar_val*j
    
     Inputs:
        - A: Given matrix
        - ith_col: i-th col
        - jth_col: j-th col
        - scalar_val: scalar value
        
    Output:
        - A: Resultant col updated matrix
    """
    
    I = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    I = np.eye(len(A[0]))
    I = elementary_ops_change_row(I, jth_col, ith_col, scalar_val)
    A = matrix_multiplication(A, I)
    
            
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, I


def sweep_out_row(
    A: np.array,
    ith_row: int,
    pivot_element: Tuple[int, int]
)->np.array:
    """
    Sweep out a i-th row based on the given pivot element
    
    Inputs:
        - A: Given matrix
        - ith_row: row to sweep out
        - pivot_element pivot element
        
    Output:
        - A: Resultant row sweep out matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    A = elementary_ops_scale_col(np.array(A,dtype = float), pivot_element[1], 1 / A[pivot_element[0]-1, pivot_element[1]-1])
    for i in range(len(A[0])):
        if i != pivot_element[1]-1:
            A = elementary_ops_change_col(A, i+1, pivot_element[1], -A[pivot_element[0]-1, i])
    
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
    
    return A

    
def sweep_out_row_mult(
    A: np.array,
    ith_row: int,
    pivot_element: Tuple[int, int]
)->np.array:
    """
    Sweep out a i-th row based on the given pivot element
    
    Inputs:
        - A: Given matrix
        - ith_row: row to sweep out
        - pivot_element pivot element
        
    Output:
        - A: Resultant row sweep out matrix
    """
    
    E_ops = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    E_ops = np.eye(len(A[0]))
    B = elementary_ops_scale_row(E_ops.copy(), pivot_element[1], 1 / A[pivot_element[0]-1, pivot_element[1]-1])
    A = matrix_multiplication(A, B)
    for i in range(len(A[0])):
        if i != pivot_element[1]-1:
            B = elementary_ops_change_row(E_ops.copy(), pivot_element[1], i+1, -A[pivot_element[0]-1, i])
            A = matrix_multiplication(A, B)
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
    
    return A, E_ops
    
    
def sweep_out_col(
    A: np.array,
    ith_col: int,
    pivot_element: Tuple[int, int]
)->np.array:
    """
    Sweep out a i-th column based on the given pivot element
    
    Inputs:
        - A: Given matrix
        - ith_col: column to sweep out
        - pivot_element pivot element
        
    Output:
        - A: Resultant column sweep out matrix
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    A = elementary_ops_scale_row(np.array(A,dtype = float), pivot_element[0], 1 / A[pivot_element[0]-1, pivot_element[1]-1])
    for i in range(len(A)):
        if i != pivot_element[0]-1:
            A = elementary_ops_change_row(A, i+1, pivot_element[0], -A[i, pivot_element[1]-1])
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
    
    return A


def sweep_out_col_mult(
    A: np.array,
    ith_col: int,
    pivot_element: Tuple[int, int]
)->Tuple[np.array, np.array]:
    """
    Sweep out a i-th column based on the given pivot element
    
    Inputs:
        - A: Given matrix
        - ith_col: column to sweep out
        - pivot_element pivot element
        
    Output:
        - A: Resultant column sweep out matrix
        - E_ops: Product of all the elementary operations
    """
    
    E_ops = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    E_ops = np.eye(len(A))
    B = elementary_ops_scale_row(E_ops.copy(), pivot_element[0], 1 / A[pivot_element[0]-1, pivot_element[1]-1])
    A = matrix_multiplication(B, A)
    for i in range(len(A)):
        if i != pivot_element[0]-1:
            B = elementary_ops_change_row(E_ops.copy(), i+1, pivot_element[0], -A[i, pivot_element[1]-1])
            A = matrix_multiplication(B, A)
   
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
    
    return A, E_ops


def reduced_echelon_form(
    A: np.array
)-> np.array:
    """Reduction to echelon form of a matrix.
    
    Inputs:
        - A: Given matrix
        
    Output:
        - A: Echelon form of A
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    r=0
    for i in range(len(A[0])):
        for j in range(r,len(A)):
            if A[j][i]!=0:
                k = A[j][i]
                A = elementary_ops_interchange_rows(A, r+1, j+1)
                A = elementary_ops_scale_row(A, r+1, 1/k)
                for l in range(r+1,len(A)):
                    m = A[l][i] 
                    if m != 0:
                        A = elementary_ops_change_row(A, l+1, r+1, m*(-1))
                r+=1
                j = len(A)
                break
                        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def reduced_upper_triangular_form(
    A: np.array
)-> np.array:
    """Reduction to upper triangular form of a square matrix.
    
    Inputs:
        - A: Given matrix
        
    Output:
        - A: Upper triangular form of A
    """
    
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[j][i] != 0:
                r = A[i,i]
                k = A[j,i]
                A = elementary_ops_change_row(np.array(A,dtype = float), j+1, i+1, -k / r)
        
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


def reduce_non_sigular_matrix_to_identity(
    A: np.array
)-> Tuple[np.array, np.array]:
    """Reduce a non-singular matrix to a identity matrix.
    
    Inputs:
        - A: Given matrix
        
    Output:
        - I: Identity matrix
    """
    
    INV_A = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    A=A.astype(float)
    n = A.shape[0]
    INV_A = np.eye(n)  # Initialize the inverse matrix with an identity matrix

    for i in range(n):
        # Find the pivot element
        pivot = A[i, i]

        # Apply the same row operation to both matrices to transform A into an identity matrix
        A[i] /= pivot
        INV_A[i] /= pivot

        for j in range(n):
            if j != i:
                factor = A[j, i]
                A[j] -= factor * A[i]
                INV_A[j] -= factor * INV_A[i]
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, INV_A


def generate_random_linear_system(
    m: int,
    n: int,
    l: int = 9,
)->Tuple[np.array, np.array, np.array]:
    """
    Generate a random system of linear equation m-equation with n-unknown (with integer coefficients)
    
    Inputs:
        - m: Number of equations
        - n: Number of unknowns
        - l: range of random integers
        
    Outputs:
        - A: Coefficient matrix
        - b: right-hand vector
        - x: soluation (its just for cross check)
    """
    
    A = []
    b = []
    x = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    A=np.random.uniform(-l,l,size=(m,n))
    x=np.random.uniform(-l,l,size=(n,1))
    b=matrix_multiplication(A,x)
    
    
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, b, x
    
    
def soln_n_equations_n_unknowns(
    A: np.array,
    b: np.array
)-> np.array:
    """Solution of a system of linear equation Ax=b(n equations with n unknowns) using matrix inverse method.
    
    Inputs:
        - A: Given coefficient matrix
        - b: Given right-hand vector
        
    Output:
        - x_est: Soluation of Ax=b
        - INV_A: Inverse of A
    """
        
    x_est = []
    INV_A = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    INV_A=reduce_non_sigular_matrix_to_identity(A)[1]
    x_est=matrix_multiplication(INV_A,b)
    
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return x_est, INV_A


def reduce_to_hcf_matrix(
    A: np.array,
    num_rows: int = None,
    num_cols: int = None,
)-> np.array:
    """Reduction to HCF form of a matrix.
    
    Inputs:
        - A (numpy array): Given matrix
        - num_rows (int): number of rows want to reduced
        - num_cols (int): number of cols want to reduced
        
    Output:
        - A (numpy array): HCF form of A
        - E_ops (numpy array): Transforming matrix (product of sequence of elementary row operations)
    """
    
    
    E_ops = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    A = np.array(A)
    E_op=[]
    num_rows = A.shape[0]
    num_cols = A.shape[1]
    i=0
    j=0
    while i < num_rows and j < num_cols:
        if A[i, j] != 0:
            A,E1= sweep_out_col_mult(A, j , (i,j))
            E_op.append(E1)
            j += 1
            i = j
        else:
            done=0
            for k in range(i + 1, num_rows):
                if A[k, j] != 0:
                    done=1
                    A,E2= elementary_ops_interchange_rows_mult(A, i , k )
                    E_op.append(E2)
                    A,E3= sweep_out_col_mult(A, j , (i,j))
                    E_op.append(E3)
                    break
            if (done==1):
                continue
            else:
                for m in range(i):
                    if(A[m,j]!=0 and A[m,m]==0):
                        A,E4= elementary_ops_interchange_rows_mult(A, i, m )
                        E_op.append(E4)
                        A,E5= sweep_out_col_mult(A, j , (i,j))
                        E_op.append(E5)
                        break
                        
            j += 1
            i = j
    E_ops = np.eye(E_op[0].shape[0])

    for matrix in E_op:
        E_ops = np.dot(E_ops, matrix)
        
    
              
                        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, E_ops

def soln_m_equations_n_unknowns(
    A: np.array,
    b: np.array
)-> np.array:
    """Solution of a system of linear equation Ax=b(m equations with n unknowns) using hermite cannonical normal form.
    
    Inputs:
        - A (numpy array): Given coefficient matrix
        - b (numpy vector/array): Given right-hand vector
        
    Output:
        - x_est (numpy vector/array): Solution of Ax=b
        - HCF_A (numpy array): HCF of A
    """
    
    x_est = []
    HCF_A = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    m=A.shape[0]
    n=A.shape[1]
    g_inv=[]
    if m != n and m >n :
        zero_column = np.zeros((m, 1))
        A = np.hstack((A, zero_column))
    elif m!=n and m < n :
        zero_row = np.zeros((1, n))
        A = np.vstack((A, zero_row))
    
    g_inv=np.linalg.pinv(A)

    HCF_A=reduce_to_hcf_matrix(A)[0]
    x_est=matrix_multiplication(g_inv,b)
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return x_est, HCF_A


def determinant_matrix(
    A: np.array,
)-> float:
    """Find the determinant of a square matrix.
    
    Inputs:
        - A (numpy array): Given matrix
        
    Output:
        - det_value (float): determinant of A
    """
    
    
    det_value = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    det_A= reduced_upper_triangular_form(A)
    value=1
    for i in range (len (det_A[0]) ):
        value = value * det_A[i, i]
    det_value=value
              
                        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return det_value



def soln_n_equations_n_unknowns_cramers_rule(
    A: np.array,
    b: np.array
)-> np.array:
    """Solution of a system of linear equation Ax=b(n equations with n unknowns) using Cramer's rule.
    
    Inputs:
        - A (numpy array): Given coefficient matrix
        - b (numpy vector/array): Given right-hand vector
        
    Output:
        - x_est (numpy vector/array): Solution of Ax=b
    """
        
    x_est = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    n = len(b)
    x_est = np.zeros(n)

    det_A = determinant_matrix(A)

    if det_A == 0:
        print("The system is either inconsistent or has infinitely many solutions.")
        return x_est

    for i in range(n):
        matrix_i = A.copy()
        matrix_i[:, i] = b.flatten()

        det_i = determinant_matrix(matrix_i)
        x_est[i] = det_i / det_A

    x_est=x_est.reshape(-1,1)
    
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return x_est


def factorize_to_lu_matrix(
    A: np.array
)-> Tuple[np.array, np.array]:
    """LU factorization of a square non-sngular matrix.
    
    Inputs:
        - A: Given matrix
        
    Output:
        - L: Lower triangular (normal) matrix
        - U: Upper triangular matrix
    """
    
    L = []
    U = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#

    rows, cols = A.shape
    # Initialize matrices L and U
    L = np.eye(rows, dtype=float)
    U = A.astype(float)

    for k in range(rows - 1):
        for i in range(k + 1, rows):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]  
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return L, U


def soln_n_equations_n_unknowns_lu_factorization(
    A: np.array,
    b: np.array
)-> np.array:
    """Solution of a system of linear equation Ax=b(n equations with n unknowns) using LU factorization.
    
    Inputs:
        - A (numpy array): Given coefficient matrix
        - b (numpy vector/array): Given right-hand vector
        
    Output:
        - x_est (numpy vector/array): Solution of Ax=b
    """
        
    x_est = []
    ############################################################################
    #                             Your code will be here                       #
    #--------------------------------------------------------------------------#
    rows, cols = A.shape

    # Perform LU decomposition
    L, U = factorize_to_lu_matrix(A)

    # Solve Ly = b for y using forward substitution
    y = np.zeros_like(b, dtype=float)
    for i in range(rows):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y for x using backward substitution
    x_est = np.zeros_like(b, dtype=float)
    for i in range(rows - 1, -1, -1):
        x_est[i] = (y[i] - np.dot(U[i, i + 1:], x_est[i + 1:])) / U[i, i]
    
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return x_est

if __name__ == '__main__':  
    
    pass







