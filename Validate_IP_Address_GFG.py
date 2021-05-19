def isValid(s):
    l = s.split('.')
    if s.count('.') != 3:
        return 0
    for i in range(len(l)):
        if l[i].isdigit() == False or int(l[i]) < 0 or int(
                l[i]) > 255 or (l[i][0] == '0' and len(l[i]) != 1):

            return 0

    return 1


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        if (isValid(s)):
            print(1)
        else:
            print(0)

# } Driver Code Ends