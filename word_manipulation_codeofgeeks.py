ans=[]
s=input()
uc=sorted(set(s.upper()))
for i in range(len(uc)):
    news=''
    for j in s:
        if uc[i]==j.upper():
            news+=j
    ans.append(news)
answer=''
i=0
j=len(ans)-1
while(i<=j):
    if ans[i]==ans[j]:
        answer+=ans[i]
    else:
        answer+=ans[i]+ans[j]
    i+=1
    j-=1
print(answer)
