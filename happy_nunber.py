happnumber=[]
for m in range(1,100):
    L = []
    n=str(m)
    while(1):
        N = 0
        ct = 0
        for j in n:
            N=int(j)**2+N
        # print(str(N))
        L.append(N)
        if N==1:
            print('True')
            happnumber.append(m)
            break
        for k in range(len(L)-1):
            if L[len(L)-1] ==L[k]:
                ct=ct+1
                break
        if ct==1:
            print('False')
            break
        n=str(N)

print(happnumber)


