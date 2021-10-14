# Python3 program to print the string
# in given pattern
 
# Function to print the string
def printStringAlternate(string):
 
    occ = {}
 
    # Start traversing the string
    for i in range(0, len(string)):
 
        # Convert uppercase to lowercase
        temp = string[i].lower()
 
        # Increment occurrence count
        occ[temp] = occ.get(temp, 0) + 1
 
        # If count is odd then print the character
        if occ[temp] & 1:
            print(string[i], end = "")
 
    print()
 
# Driver code
if __name__ == "__main__":
 
    string = "Geeks for geeks"
    string2 = "It is a long day Dear"
 
    printStringAlternate(string)
    printStringAlternate(string2)
 
# This code is contributed by Rituraj Jain
