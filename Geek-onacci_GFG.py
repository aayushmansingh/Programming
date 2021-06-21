#Problem Link: https://practice.geeksforgeeks.org/problems/geek-onacci-number/0/?fbclid=IwAR2RvA6h5b5XC-EbfKVTt1w2bJUUyYTfrvOR5bzFiCphTkBmaPS5WI6FgbI


#code
for tc in range(int(input())):
    a, b, c, n = map(int, input().split())
    for i in range(n - 3):
        s = a + b + c
        a = b
        b = c
        c = s
    print(s)
