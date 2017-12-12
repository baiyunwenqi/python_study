x=input("please enter an integer:")
x=int(x)
if x<0:
    x=0
    print('Negative changed to zero')
elif x==0:
    print('zero')
elif x==1:
    print('Single')
else:
    print('More')