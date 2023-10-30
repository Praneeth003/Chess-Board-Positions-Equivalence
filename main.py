from kp import *
import numpy as np

# posi1 = 'b2K4;2p5;3k4;1Q6;5P2;1B6;16'
# posi2 = '16;1B6;5P2;1Q6;3k4;2p5;b2K4'

posi1 = input("Enter the first board position:")
posi2 = input("Enter the second board position:")
A = np.array(position(posi1))
X = np.array(position(posi2))

#Function to rotate the position of board in clockwise direction
def cwise_rotation(P):
    transposed_matrix = np.transpose(P)
    cwise_rotated_matrix = np.flip(transposed_matrix, axis=1)
    return cwise_rotated_matrix

#Function to project the board along the horizontal axis
def projection_horizontal(P):
    new_matrix = np.flip(P, axis=0)
    return new_matrix

#Function to project the board along the vertical axis
def projection_vertical(P):
    new_matrix = np.flip(P, axis=1)
    return new_matrix

# Function to check if there exitsts any pawn in the board 
def exitsPawn(A):
    for row in A:
        if 'p' in row or 'P' in row:
            return True
    return False

# If pawn exists, only check with the orginal position and its vertical projection position
# No need to check with other possibilities to preserve the game scenario
if(exitsPawn(A)):
    AV = projection_vertical(A)
    M = [A, AV]
    isEquivalent = False
    for i in M:
        if np.array_equal(X, i):
            isEquivalent = True
            break
    if isEquivalent:
        print(" There is an equivalence")
    else:
        print(" There is no equivalence")

else:
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

    M = [A, B, C, D, M1, M2, M3, M4]
    isEquivalent = False

    for i in M:
        if np.array_equal(X, i):
            isEquivalent = True
            break

    if isEquivalent:
        print(" There is an equivalence")
    else:
        print(" There is no equivalence") 
 
