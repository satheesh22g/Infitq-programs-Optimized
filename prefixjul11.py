ip="xxabcxxabcxx"
prefix=[]
suffix=[]
res=[]
for i in range((len(ip)//2)+1):
    prefix.append(ip[:i])
for j in range(1,len(ip)//2+1):
    suffix.append(ip[-j:])
for i in prefix:
    if i in suffix:
        res.append(i)
print(len(max(res)))