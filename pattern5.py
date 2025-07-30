n = int(input("Enter value of n "))
for i in range(n, 0, -1):            
    for j in range(65, 65 + i):      
        print(chr(j), end=' ')
    print()
