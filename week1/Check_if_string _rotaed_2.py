s1 = input("Enter string1 : ")
s2 = input("Enter string2 : ")

s = s1[2:] + s1[0:2]
 
if s == s2:
    print("True")
else:
    print("False")
""" Sample Input:
    
    sathesh
    shhtesa

    sample output:
    False
"""