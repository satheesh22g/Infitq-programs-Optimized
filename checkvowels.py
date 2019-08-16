#Program to accept the strings which contains all vowels
ip=input()
vowels=["a","e","i","o","u"]
ip.lower()
new=[]
for i in ip:
    if i in vowels:
        new.append(i)
if len(vowels)==len(new):
    print("valid")
else:
    print("invalid")

