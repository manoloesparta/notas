i = len(numList) - 1
 
while i > 1:
 
    j = 0
 
    while j < i:
 
        # Tracks the comparison of index values
        print("\nIs {} > {}".format(numList[j], numList[j+1]))
        print()
 
        # If the value on the left is bigger switch values
        if numList[j] > numList[j+1]:
 
            print("Switch")
 
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
 
        else:
            print("Don't Switch")
 
        j += 1
 
        # Track changes to the list
        for k in numList:
            print(k, end=", ")
        print()
 
    print("END OF ROUND")
 
    i -= 1
 
for k in numList:
    print(k, end=", ")
print()