'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    # Print leading hyphens
    print(" " * (n - i), end="")
    
    # Print stars
    print("* " * i)
