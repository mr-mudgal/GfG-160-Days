# User function Template for python3
class Solution:
	def kthMissing(self, arr, k):
		current = 1
		missing_count = 0

		for num in arr:
			while current < num:
				missing_count += 1
				if missing_count == k:
					return current
				current += 1
			current = num + 1

		return arr[-1] + (k - missing_count)


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
		ans = ob.kthMissing(A, D)
		print(ans)
		print("~")

# } Driver Code Ends
