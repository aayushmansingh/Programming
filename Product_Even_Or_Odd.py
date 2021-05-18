class Solution:
    def EvenOdd(self, n1, n2):
        last1 = n1 % 10
        last2 = n2 % 10
        if (last1 * last2) % 2 == 0:
            return 1
        else:
            return 0


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = int(input().strip())
        b = int(input().strip())
        ob = Solution()
        ans = ob.EvenOdd(a, b)
        print(ans)
# } Driver Code Ends