str1 = input("Enter string1 : ")
str2 = input("Enter string2 : ")
k = int(input())

lst = []
if(len(str1) != len(str2)):
    print("No")

s1 = list(str1)
s2 = list(str2)
s1.sort()
s2.sort()

for i in range(len(str1)):
    if(s1[i] != s2[i]):
        lst.append(s2[i])

if(len(lst) <= k):
    print("Yes")
else:
    print("No")

""" Sample Input1:
    
    Enter string1 : anagram
    Enter string2 : grammar
    3

    Sample Output1:

    Yes

    Sample Input2:
    
    Enter string1 : care
    Enter string2 : cool
    1

    Sample Output2:

    No

"""