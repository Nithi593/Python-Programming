s1 = input("Enter string1 : ")
s2 = input("Enter string2 : ")

if(len(s1) != len(s2)):
    print("No")
elif(sorted(s1) != sorted(s2)):
    print("No")
elif("".join(s1[:2]) == "".join(s2[len(s2)-2:])):
    print("Yes")
else:
    print("No")

