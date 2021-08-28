str = input("Enter string : ")
str1 = str.split(" ")
#str = str1[::-1]
st = ""
for i in str1:
    st = i + " " + st
print(st)

""" Sample Input:
    
    Enter String : Computer Science

    Sample Output:

    Science Computer
"""