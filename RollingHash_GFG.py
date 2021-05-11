str = input()
s, c = 0, 0
for i in str:
    s += ord(i)
    c += 1
print(s // c)
