##Complete this function
def leftIndex(arr, N, X):
    for i in range(N):
        if arr[i] == X:
            return i
    return -1


#{
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        x = int(input())

        print(leftIndex(A, N, x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends