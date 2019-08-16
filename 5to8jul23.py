ip=list(map(int,input().split()))
print(sum(ip[:ip.index(5)])+int("".join(list(map(str,ip[ip.index(5):ip.index(8)+1]))))+sum(ip[ip.index(8)+1:]))


