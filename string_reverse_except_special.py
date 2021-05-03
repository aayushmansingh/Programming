s=input()
l=[]
ans=''
pre_def='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for i in s:
    if i in pre_def:
        ans = i+ans
        
for i in range(len(s)):
    if s[i] not in pre_def:
        ans=list(ans)
        ans.insert(i,s[i])
        ans=''.join(ans)
print(ans) 