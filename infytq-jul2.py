def find(s):
    return [x for x in [s[i:j+1] for i in range(len(s)) for j in range(i, len(s))]  if len(x)>=3]
def rem(s):
    l=[]
    for i in s:
        if i.lower() not in [i.lower() for i in list(set(l))]:
            l.append(i)
    return ''.join(l)
# s="Ba@Aaaaabbx"
s=input()
# print(rem(s))
c= find(s)
c.remove(s)
l = [ i for i in map(rem ,c) if len(i) >=3 ]
x=[i for i in l if len(i)==max(map(len, l))]
print(-1 if len(x)==0 else x[0])
