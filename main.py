from inputConverter import *
import numpy as np
import os

print("If you want to check for equivalence between two positions, enter 1")
print("If you want to check if the position or its equivalent position is already in the database, enter 2")
print("If you want to add a new position to the database, enter 3")


# Function to open a file and read position from it
def readFile(l):
    with open('./database/tempData/' + l + '.txt', 'r') as file:
        content = []
        for line in file:
            content.append(line.strip())
    # content holds the data in List of Strings format
    return np.array(content)

# Function to check if there exitsts any pawn in the board 
def exitsPawn(A):
    for row in A:
        if 'p' in row or 'P' in row:
            return True
    return False

# Function to generate all the possible positions for a given board position and store them in separate files
def generatePositions(A):
    # Function to rotate the position of board in clockwise direction
    def cwise_rotation(P):
        transposed_matrix = np.transpose(P)
        cwise_rotated_matrix = np.flip(transposed_matrix, axis=1)
        return cwise_rotated_matrix

    # Function to project the board along the horizontal axis
    def projection_horizontal(P):
        new_matrix = np.flip(P, axis=0)
        return new_matrix

    # Function to project the board along the vertical axis
    def projection_vertical(P):
        new_matrix = np.flip(P, axis=1)
        return new_matrix

    # Function to create a file and write corresponding position into it
    def createFile(l, m):
        # Open a file for writing
        with open('./database/tempData/' + l + '.txt', 'w') as file:
            for row in m:
                # Convert row into string
                rowString = str(row)
                # Write each row to the file
                file.write(rowString + '\n')
    
    # All the possible positions assigned to respective variables
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

    # Using dictionary to help placing positions in corresponding filenames
    dictionary = {
        "A" : A,
        "B" : B,
        "C" : C,
        "D" : D,
        "M1" : M1,
        "M2" : M2,
        "M3" : M3,
        "M4" : M4
    }

    # Iterating to create all the respective files
    for key, value in dictionary.items():
        createFile(key, value)


choice = int(input("Enter your choice: "))
if choice == 1:
    posi1 = input("Enter the first board position:")
    posi2 = input("Enter the second board position:")
    A = np.array(position(posi1))
    X = np.array(position(posi2))
    
    # Generating all the possible positions for the first board position and storing them in separate files
    generatePositions(A)

    # Converting X into List of Strings format
    Y =[]
    for row in X:
        Y.append(str(row))
    Y = np.array(Y)

    # If pawn exists, only check with the orginal position and its vertical projection position
    # No need to check with other possibilities to preserve the game scenario
    #Else, check with all the possible positions
    if(exitsPawn(A)):
        M = ["A", "M2"]
    else:
        M = ["A","B","C","D","M1","M2","M3","M4"]
    
    flag = False
        
    for i in M:
        if np.array_equal(Y, readFile(i)):
            flag = True
            break
    
    if flag == True:
        print("There is an equivalence!!")
    else:
        print("There is no equivalence!!")

  

elif choice == 2:
    posi = input("Enter the board position:")
    A = np.array(position(posi))
    
    # Using os.walk to iterate through all the files in the directory
    path, dirs, files = next(os.walk("./database/storedData"))

    generatePositions(A)

    #if there exitst a pawn in the board, then only check with the original position and its vertical projection position, 
    #else check with all the possible positions
    if(exitsPawn(A)):
        M = ["A", "M2"]
    else:
        M = ["A","B","C","D","M1","M2","M3","M4"]
    

    flag = False
    
    # Iterating through all the files in the directory
    for i in files:
        with open('./database/storedData/' + i, 'r') as file:
            content = []
            for line in file:
                content.append(line.strip())
        # content holds the data in List of Strings format
        for j in M:
            if np.array_equal(np.array(content), readFile(j)):
                flag = True
                break
        if flag == True:
            break
    
    if flag == False:
        print("This position or its equivalent position is not in the database!!")
    
    else:
        print("The position or its equivalent position exists in the database!!")


elif choice == 3:
    posi = input("Enter the board position:")
    A = np.array(position(posi))
    
    # Using os.walk to iterate through all the files in the directory
    path, dirs, files = next(os.walk("./database/storedData"))

    generatePositions(A)

    #if there exitst a pawn in the board, then only check with the original position and its vertical projection position, 
    #else check with all the possible positions
    if(exitsPawn(A)):
        M = ["A", "M2"]
    else:
        M = ["A","B","C","D","M1","M2","M3","M4"]
    

    flag = False
    
    # Iterating through all the files in the directory
    for i in files:
        with open('./database/storedData/' + i, 'r') as file:
            content = []
            for line in file:
                content.append(line.strip())
        # content holds the data in List of Strings format
        for j in M:
            if np.array_equal(np.array(content), readFile(j)):
                flag = True
                break
        if flag == True:
            break
    
    if flag == True:
        print("The position or its equivalent position already exists in the database!!")

    else:
        # Creating a new file and writing the position into it
        with open('./database/storedData/' + str(len(files)+1) + '.txt', 'w') as file:
            for row in A:
                # Convert row into string
                rowString = str(row)
                # Write each row to the file
                file.write(rowString + '\n')
        print("The position is added to the database!!")

    
    

        