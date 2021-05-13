##Complete this code
def countOnes(arr, N):
    c = 0
    for i in arr:
        if i == 1:
            c += 1
    return c


#{
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(countOnes(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends