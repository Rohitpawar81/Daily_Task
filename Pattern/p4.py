
'''
    0
   01
  010
 0101
01010
'''


n = int(input("Enter the number of rows: "))

for i in range(1, n+1):  # Loop for each row
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print alternating 1s and 0s
    for j in range(i):
        print(j % 2, end="")
    
    # Move to the next line
    print()
