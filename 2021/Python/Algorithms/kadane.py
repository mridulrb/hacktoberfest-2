class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        max_so_far=0
        max_here=0
        
        for i in range (len(arr)):
            max_so_far=max_so_far+arr[i]
            if (max_so_far<0):
                max_so_far=0
            if (max_so_far>max_here):
                max_here=max_so_far
        if(max_here==0 or max_so_far<0):
            arr.sort()
            return(arr[N-1])
        else:
            return(max_here)
            
        ##Your code here



import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1

