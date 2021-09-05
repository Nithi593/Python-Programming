def longestPrefixSuffix(str):
    n = len(str)
    for i in range(n//2,0,-1):
        pre = str[0 : i]
        suf = str[n-i : n]
        if pre == suf:
            return len(pre) 
    return 0
    
str = input("Enter string : ")
print(longestPrefixSuffix(str))

