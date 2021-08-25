num = int(input("Enter the number : "))

if(num < 0):
    print("Not Divisible")
elif(num == 0 or num % 7 == 0):
    print(num,"is divisible by 7")
else: 
    print("Not Divisible")

""" Sample Input1:
    
    Enter the number : 56

    Sample Output1:

    56 is divisible by 7

    Sample Input2:
    
    Enter the number : -9

    Sample Output2:

    Not Divisible

"""