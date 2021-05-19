class Solution:
    def repeatedSubtraction(self, A, B):
        steps = 0
        while A > 0 and B > 0:
            if A > B:
                steps += A // B
                A = A % B
            else:
                steps += B // A
                B = B % A

        return steps


#{
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().strip().split(" "))
        ob = Solution()
        print(ob.repeatedSubtraction(A, B))
# } Driver Code Ends