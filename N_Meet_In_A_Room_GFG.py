class Solution:

    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here
        meet = []
        maxi = 1
        for meeting in range(n):
            meet.append((start[meeting], end[meeting]))
        meet.sort(key=lambda key: key[1])  #sorting on basis of end timing

        meet_start, meet_end = meet[0][0], meet[0][1]
        for i in range(1, n):
            if meet_end < meet[i][0]:
                maxi += 1
                meet_end = meet[i][1]
        return maxi


#{
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(n, start, end))
# } Driver Code Ends