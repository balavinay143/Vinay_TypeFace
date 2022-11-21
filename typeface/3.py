a=int(input())
l=['0','1','2','5','6','8','9']
x=len(l)
q=""
while a>0:
    q=q+l[a%x]
    a//=x
print(int(q[::-1]))
