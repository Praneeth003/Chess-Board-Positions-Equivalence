def position(posi):
    #Removing white spaces in the string
    posi = posi.replace(" ","")
    #print("position is:" + posi)


    # Converting the string into list
    list = posi.split(";")
    #print("List Representation is:")
    #print(list)


    # This list stores information in terms of rows.
    rowList = []


    # Function to split digit entries into rows. For example 24 into 8,8,8
    def splitting(i):
        j = int(i)
        if j == 8:
            rowList.append(str(j))
        else:
            rowList.append(str(8))
            splitting(str(j - 8))
        

    # Splitting into a list of rows
    for i in list:
        if i.isdigit():
            splitting(i)
        else:
            rowList.append(i)
    #print("Row List is:")
    #print(rowList)



    # This function takes: a string and an empty string as input
    # It returns the list with appropriate ' ' as required
    def helper(str1,ch):
        for j in str1:
            if j.isdigit():
                if int(j) == 0:
                    continue
                elif int(j) == 1:
                    ch.append(' ')
                else:
                    ch.append(' ')
                    helper(str(int(j) - 1),ch)
            else:
                ch.append(j)
        return ch

    List_Of_Lists = []
    for k in range(8):
        List_Of_Lists.append(helper(rowList[k],[]))
    #print(List_Of_Lists)
    return List_Of_Lists


                




