class Solution:
	def peakElement(self, arr):
		for i in range(len(arr)):
			if (len(arr) == 1) or (i == 0 and arr[i] > arr[i + 1]):
				return 0
			elif i < len(arr) - 1 and arr[i - 1] < arr[i] > arr[i + 1]:
				return i
			elif arr[i] > arr[i - 1] and i == len(arr) - 1:
				return i


# {
# Driver Code Starts
if __name__ == "__main__":
	t = int(input())  # Read number of test cases
	for _ in range(t):
		# Read input and split it into a list of integers
		arr = list(map(int, input().split()))
		# Create a Solution object and calculate the result

		index = Solution().peakElement(arr)
		n = len(arr)
		flag = False
		if index < 0 or index >= n:
			flag = False
		else:
			if index == 0 and n == 1:
				flag = True
			elif index == 0 and arr[index] > arr[index + 1]:
				flag = True
			elif index == n - 1 and arr[index] > arr[index - 1]:
				flag = True
			elif index > 0 and index < n - 1 and arr[
				index - 1] < arr[index] and arr[index] > arr[index + 1]:
				flag = True
			else:
				flag = False

		if flag:
			print("true")
		else:
			print("false")
		print("~")

# } Driver Code Ends
