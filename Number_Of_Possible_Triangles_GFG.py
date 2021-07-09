class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        #code here
        arr.sort()
        count = 0
        for i in range(n - 2):
            k = i + 2
            for j in range(i + 1, n - 1):
                while (k < n and arr[i] + arr[j] > arr[k]):
                    k += 1
                count += k - j - 1
        return count


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr, n))

# } Driver Code Ends