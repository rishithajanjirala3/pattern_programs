n=int(input('enter number of rows: '))
for i in range(1,n+1):
    print('', end=" ")
    for j in range(n): 
        print(i, end=" ")  
    print()

#output:
# enter number of rows: 3
#  1 1 1 
#  2 2 2 
#  3 3 3