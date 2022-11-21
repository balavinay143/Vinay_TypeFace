n=int(input())
l=['0','1','2','5','6','8','9']
x=len(l)
s=""
while n>0:
    s=s+l[n%x]
    n//=x
print(int(s[::-1]))