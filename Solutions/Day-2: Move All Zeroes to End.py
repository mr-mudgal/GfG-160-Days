"""
Given an array arr[]. 
Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements.
Do the mentioned change in the array in place.
"""

#User function Template for python3
class Solution:
	def pushZerosToEnd(self,arr):
		count = 0

		for i in arr:
			if i == 0:
				count += 1
		[arr.remove(0) for _ in range(count)]
		arr += [0]*count

		return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends

# ⎬coded by⎨ ⌘‣ Mr. Mudgal
