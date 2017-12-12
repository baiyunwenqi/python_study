N=int(input())
M=int((N+1)/2)
for i in range(1,M+1):
  C =''
  for j in range(N):
      if j<=M+i-2 and j>=M-i:
          C=C+'*'
      else:
          C=C+' '
  print(C)