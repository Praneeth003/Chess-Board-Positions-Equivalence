import numpy as np

A = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ])

X = np.array([
    [16,12,8,4],
    [15,11,7,3],
    [14,10,6,2],
    [13,9,5,1]
    ])

def cwise_rotation(P):
    transposed_matrix = np.transpose(P)
    cwise_rotated_matrix = np.flip(transposed_matrix, axis=1)
    return cwise_rotated_matrix

def projection_horizontal(P):
    new_matrix = np.flip(P, axis=0)
    return new_matrix

def projection_vertical(P):
    new_matrix = np.flip(P, axis=1)
    return new_matrix

M1 = projection_horizontal(A)
M2 = projection_vertical(A)

B = cwise_rotation(A)
M3 = projection_horizontal(B)
M4 = projection_vertical(B) 

C = cwise_rotation(B)
M5 = projection_horizontal(C)
M6 = projection_vertical(C)

D = cwise_rotation(C)
M7 = projection_horizontal(D)
M8 = projection_vertical(D)

print(M1)
print("\n")
print(M2)
print("\n")
print(M3)
print("\n")
print(M4)
print("\n")
print(M5)
print("\n")
print(M6)
print("\n")
print(M7)
print("\n")
print(M8)

print("The second matrix is: ")
print(X)

if np.array_equal(X, M8):
    print(" There is an equivalence")