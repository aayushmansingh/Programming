import math
test = 1
# test = int(input())

# for tc in range((test)):
    # Write your code from here....

def foo(num,l):
    for i in num:
        if int(i)==l:
            return True
    return False



n=input()
l=n.split(",")

ans=''
for i in l:
    k=i.split(":")
    # print(k)
    name=k[0]
    num=k[1]
    length=len(name)
    # print(name,length)
    
    while(length>=0):
        if foo(num,length):
            # print("break")
            ans+=name[length-1]
            # print(length)
            break
        length-=1
    if(length<0):
        ans+="X"


print(ans)

            
      
