#!/usr/bin/env python
# coding: utf-8
"""
-----------------------------------------------------------------------------
Assignment-3: Matrix computation exercise using python and numpy
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
    zipped_list= zip(x,y) #If two vectors are of different order then zipping and unzipping them will make the order same..
    x,y = zip(*zipped_list) #by removing extra components(which would have become zero while doing dot product)
    prod=0
    for i in range (len(x)):
        prod = prod+x[i]*y[i]
    val.append(prod)
    if np.dot(x,y) == prod:
        print("vector dot product is valid")
    else:
        print("vector dot product is invalid")
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
        val1 = []
        for j in range(len(y[0])):
            sum = 0
            for k in range(len(y)):
                sum+= x[i][k]*y[k][j]
            val1.append(sum)
        val.append(val1)
    val = np.array(val)
    
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
        temp=A[ith_row-1][k]
        A[ith_row-1][k]=A[jth_row-1][k]
        A[jth_row-1][k]=temp
    
    
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
    A, E_ops = elementary_ops_scale_col_mult(np.copy(A), pivot_element[1], 1 / A[pivot_element[0]-1, pivot_element[1]-1])
    for i in range(len(A[0])):
        if i != pivot_element[1]-1:
            A, B = elementary_ops_change_col_mult(np.copy(A), i+1, pivot_element[1], -A[pivot_element[0]-1, i])
            E_ops = matrix_multiplication(E_ops, B)
        
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
    A,E_ops = elementary_ops_scale_row_mult(A.copy(), pivot_element[0], 1 / A[pivot_element[0]-1, pivot_element[1]-1])
    for i in range(len(A)):
        if i != pivot_element[0]-1:
            A, B = elementary_ops_change_row_mult(A.copy(), i+1, pivot_element[0], -A[i, pivot_element[1]-1])
            E_ops = matrix_multiplication(B,E_ops)
   
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
                A = elementary_ops_interchange_rows(A, r+1, j+1)
                A = sweep_out_col(A, i+1, (r+1, i+1))
                r+=1
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
    r=0
    INV_A = np.eye(len(A))
    b = []
    for i in range(len(A[0])):
        for j in range(r,len(A)):
            if A[j][i]!=0:
                A,b = elementary_ops_interchange_rows_mult(A, r+1, j+1)
                INV_A = matrix_multiplication(b,INV_A)
                A,b = sweep_out_col_mult(A, i+1, (r+1, i+1))
                INV_A = matrix_multiplication(b,INV_A)
                r+=1
                break
        
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
    A = np.random.randint(-l,l+1,(m,n))
    x = np.random.randint(-l,l+1,(n,1))
    b = matrix_multiplication(A,x)
    
    
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A, b, x
    
    
def soln_n_equations_n_unknowns(
    A: np.array,
    b: np.array
)-> np.array:
    """Inverse of a non-singular matrix using reduced echelon form.
    
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
    I = []
    I, INV_A = reduce_non_sigular_matrix_to_identity(A)
    x_est = matrix_multiplication(INV_A,b)
    
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return x_est, INV_A

if __name__ == '__main__':  
    
    pass







