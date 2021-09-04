a = "abcba"
n = 3
def ishuiwen(a,n):
    for i in range(0,len(a)-n+1):
        if a[i:i+n:]==a[i:i+n][::-1]:
            return "YES"
    return "NO"
res=ishuiwen(a,n)
print(res)