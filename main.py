import numpy as np

A = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ])

def cwise_rotation(B):
    transposed_matrix = np.transpose(B)
    cwise_rotated_matrix = np.flip(transposed_matrix, axis=1)
    return cwise_rotated_matrix

def projection_horizontal(C):
    new_matrix = np.flip(C, axis=0)
    return new_matrix

def projection_vertical(D):
    new_matrix = np.flip(D, axis=1)
    return new_matrix

print(projection_horizontal(A))
print(projection_vertical(A))
