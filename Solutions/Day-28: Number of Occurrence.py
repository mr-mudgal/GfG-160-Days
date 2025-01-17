from collections import Counter


class Solution:
	def countFreq(self, arr, target):
		temp = Counter(arr)
		return temp[target]


# {
# Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
	t = int(input())
	while t:
		t -= 1
		A = [int(x) for x in input().strip().split()]
		nd = [int(x) for x in input().strip().split()]
		D = nd[0]
		ob = Solution()
		ans = ob.countFreq(A, D)
		print(ans)
		print("~")

# } Driver Code Ends