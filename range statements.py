# print('i in range(5,10)')
# for i in range(5,10):
#     print(i)
# a=['mary','had','a','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equal',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

for num in range(2,10):
    if num%2==0:
        print("found an even number",num)
        continue
    print("Found a number",num)