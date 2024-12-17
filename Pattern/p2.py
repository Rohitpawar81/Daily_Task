'''
    *
   **
  ***
 ****
*****

'''

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):  # Loop for each row
    print(" " * (n - i) + "*" * i)  # Print spaces and stars in the same line
