class Solution:
    def sort012(self, a, n):
        low = 0
        high = n - 1
        mid = 0
        while (low <= high):
            if (a[low] == 0):
                a[low], a[mid] = a[mid], a[low]
                low += 1
                mid += 1
            elif (a[low] == 1):
                low += 1
            else:
                a[low], a[high] = a[high], a[low]
                high -= 1


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends