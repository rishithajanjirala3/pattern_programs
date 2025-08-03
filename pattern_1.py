'''Rule: Print a square patterns
-->outer loop for rows 
-->inner loop for columns
-->use print function with end parameter to avoid new line'''

# This code prints a square pattern 
n=int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#output:
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *