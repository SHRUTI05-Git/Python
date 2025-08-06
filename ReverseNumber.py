n = int(input("Enter a number: "))

result=0

while n !=0:
    num = n % 10
    result = result*10 + num
    n = n//10
    
print("The reverse number is:", result)
