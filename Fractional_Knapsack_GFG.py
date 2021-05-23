class Solution:
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, Items, n):
        value_by_weight = []
        curr, res = 0, 0
        x = []
        for i in Items:
            value_by_weight.append((i.value / i.weight, i.weight))
        value_by_weight = sorted(value_by_weight)[::-1]
        for i in range(n):
            if curr >= W:
                break
            elif value_by_weight[i][1] + curr < W:
                x.append(1)
            else:
                x.append((W - curr) / value_by_weight[i][1])
            curr += value_by_weight[i][1]
            res += x[i] * value_by_weight[i][0] * value_by_weight[i][1]
        return res


#{
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        Items = [Item(0, 0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2 * i]
            Items[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, Items, n))

# } Driver Code Ends