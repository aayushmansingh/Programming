//Problem video(use it for reference only): https://www.youtube.com/watch?v=g6OxU-hRGtY


//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.BigInteger;


 // } Driver Code Ends
//User function Template for Java

class Solution{
    
    //Function to return sum of count of set bits in the integers from 1 to n.
    public static int largestpowerof2beforeN(int n)
    {
        int x=0;
        while((1<<x)<=n) // 1<<x means 2 to the power of x
        {
            x+=1;
        }
        return x-1;
    }
    
    
    public static int countSetBits(int n){
        
        if(n==0)
        {
            return 0;
        }
    
        int x=largestpowerof2beforeN(n);
        
        int bitstill2powerX= x*(1<<(x-1));
        int msb2powXtoN= n- (1<<x) +1;
        
        int remaining= n-(1<<x);
        int res= bitstill2powerX + msb2powXtoN + countSetBits(remaining);
        
    
        return res;
    }
    
}

// { Driver Code Starts.

// Driver code
class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();//testcases
		int x, n;
		while(t-->0) {
	        n = sc.nextInt();//input n

		    Solution obj = new Solution();

		    System.out.println(obj.countSetBits(n));//calling countSetBits() method
		}
	}
}
  // } Driver Code Ends