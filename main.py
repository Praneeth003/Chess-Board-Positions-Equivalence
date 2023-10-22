from kp import *
import numpy as np

posi1 = 'b2K4;2p5;3k4;1Q6;5P2;1B6;16'
posi2 = '16;1B6;5P2;1Q6;3k4;2p5;b2K4'
A = np.array(position(posi1))
X = np.array(position(posi2))


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

# print(M1)
# print("\n")
# print(M2)
# print("\n")
# print(M3)
# print("\n")
# print(M4)
# print("\n")
# print(M5)
# print("\n")
# print(M6)
# print("\n")
# print(M7)
# print("\n")
# print(M8)

M = [M1, M2, M3, M4, M5, M6, M7, M8, B, C, D]
isEquivalent = False

for i in M:
    if np.array_equal(X, i):
        isEquivalent = True
        break

if isEquivalent:
    print(" There is an equivalence")
else:
    print(" There is no equivalence") 
 
    

