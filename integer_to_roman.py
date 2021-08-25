num = int(input("Enter the number : "))
val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

result = ""
for x in range(13):
    while num >= val[x]:
        result = result + rom[x]
        num = num - val[x]

print(result)

""" Sample Input:
    
    Enter the number : 2679

    Sample Output:

    MMDCLXXIX

"""