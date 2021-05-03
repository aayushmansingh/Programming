import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    m,s=map(int,input().split())
    c=0
    while(m>0):
        m-=s
        if m>=0:
            c+=1
    print(c)
