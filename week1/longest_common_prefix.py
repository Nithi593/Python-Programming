strs = ["car", "carrace", "carwash"]
strs.sort(key=len)
pref=0
dp=[]
first=strs[0]
for x in strs:
    l=0
    pref=0
    while(l<len(first) and first[l]==x[l]):
        pref=pref+1
        l=l+1
    dp.append(pref)
print(first[:min(dp)])

""" Sample Input:
    
    strs = ["car", "carrace", "carwash"]

    Sample Output:

    car

"""