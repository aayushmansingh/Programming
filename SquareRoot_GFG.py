#Complete this function
def floorSqrt(x):
    i = 1
    while (i * i <= x):
        i += 1
    return i - 1


#{
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends