#Problem Link: https://practice.geeksforgeeks.org/problems/element-appearing-once2552/1
from collections import Counter


class Solution:
    def search(self, A, N):
        # your code here
        freq = Counter(A)
        for i in freq:
            if freq[i] == 1:
                return i


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.search(arr, n))
# } Driver Code Ends
