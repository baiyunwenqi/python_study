x=input("")
c=''
for m in x:
    if ord(m)>=97 and ord(m)<=122:
        k=(ord(m)-97+3)%26+97
        m=chr(k)
    c=c+m
print(c)