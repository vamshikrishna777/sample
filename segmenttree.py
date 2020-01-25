import math
def search(ss,se,u,v,si):
    if u<=ss and v>=se:
        return ll[si]
    if v<ss or u>se:
        return 100000000
    mid=(ss+se)//2
    return min(search(ss,mid,u,v,(2*si)+1),search(mid+1,se,u,v,(2*si)+2))
def cons(l,ss,se,si):
    #print(ll)
    if ss==se:
        ll[si]=l[ss]
        return l[ss]
    mid=(ss+se)//2
    ll[si]= min(cons(l,ss,mid,(2*si)+1),cons(l,mid+1,se,(2*si)+2))
    return ll[si]
def update(ss,se,ind,val):
    if ss==se:
        l[ind]=val
        ll[ss]=val
    else:
        mid=(ss+se)//2
        if ind<=mid:
            return update(ss,mid,ind,val)
        else:
            return update(mid+1,se,ind,val)
            
o,p=map(int,input().split())       
l=list(map(int,input().split()))
n=o
x=int(math.ceil(math.log(n)/math.log(2)))
x=2*pow(2,x)-1
ll=[0]*(x)
cons(l,0,n-1,0)
while p:
    p-=1
    c,u,v=map(str,input().split())
    u=int(u)
    v=int(v)
    if c=="q":
        if u<0 or v>n-1 or v<u:
            print("invalid")
        else:
            print(search(0,n-1,u,v,0))
    else:
        update(0,n-1,u-1,v)
#print(l)
