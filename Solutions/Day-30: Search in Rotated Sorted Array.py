# User function Template for python3

class Solution:
	def search(self, arr, key):
		if key in arr:
			return arr.index(key)
		else:
			return -1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	t = int(input())

	for _ in range(t):
		A = list(map(int, input().strip().split()))
		k = int(input())
		ob = Solution()
		print(ob.search(A, k))
		print("~")

# } Driver Code Ends
