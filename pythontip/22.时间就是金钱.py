st="00:00:00"
et="00:00:10"
def tran2s(a):
    a=a.split(":")
    sum=int(a[0])*3600+int(a[1])*60+int(a[2])
    return sum
a=tran2s(st)
b=tran2s(et)
print(abs(a-b))