#code
for tc in range(int(input())):
    a, b, c, n = map(int, input().split())
    for i in range(n - 3):
        s = a + b + c
        a = b
        b = c
        c = s
    print(s)