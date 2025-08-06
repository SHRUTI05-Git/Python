n = int(input("Enter a digit: "))
original = n
result=0

while n !=0:
    num = n % 10
    result = result*10 + num
    n = n//10

if original == result:
    print("The",original, "is palindrome..")
else:
    print("The",original, "is not palindrome..")
