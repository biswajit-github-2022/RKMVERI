#!/usr/bin/env python
# coding: utf-8
"""
-----------------------------------------------------------------------------
Assignment-2: Matrix computation exercise using python and numpy
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
    
        
    #--------------------------------------------------------------------------#
    #                             End of your code                             #
    ############################################################################
        
    return A


if __name__ == '__main__':  
    
    pass







