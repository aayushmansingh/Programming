#Problem Link: https://practice.geeksforgeeks.org/problems/magical-string3653/0/


#User function Template for python3
class Solution:
    def magicalString(ob, S):
        # code here
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        S.lower()
        res = ''
        for i in range(len(S)):
            char = S[i]
            char = alpha[122 - ord(char)]
            res += char
        return res


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = str(input())

        ob = Solution()
        print(ob.magicalString(S))
# } Driver Code Ends
