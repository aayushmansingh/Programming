#Problem Link: https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1

from collections import deque


class Solution:

    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):
        q = deque()
        i, j = 0, 0
        res = []
        while (j < n):
            while q and arr[j] > q[-1]:
                q.pop()
            q.append(arr[j])
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                res.append(q[0])
                if q[0] == arr[i]:
                    q.popleft()
                i += 1
                j += 1

        return res


#{
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(arr, n, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
