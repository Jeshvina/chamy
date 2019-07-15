a=int(input())
n=int(input())
for i in range(a,(n+1)):
    o=len(str(i))
    s2=0
    j=i
    while (j>0):
     t=j%10
     s2+=t**o
     j=j//10
    if(i==s2):
      print(i)
