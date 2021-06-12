#Problem link: https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1

#Please try yourself first, before moving on to the solution.


class Solution:

    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        stack = []
        for i in range(n):
            stack.append(i)
        while (len(stack) >= 2):
            i = stack.pop()
            j = stack.pop()

            if M[i][j] == 1:
                #i knows j, therefore i can't be a celebroty
                stack.append(j)
            else:
                #j can't be a celebrity
                stack.append(i)
        celeb = stack.pop()
        for i in range(len(M)):
            if i != celeb:
                if M[i][celeb] == 0 or M[celeb][i] == 1:
                    return -1
        return celeb


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k += 1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m, n))
# } Driver Code Ends
