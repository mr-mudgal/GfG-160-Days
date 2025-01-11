class Solution:
	def mergeOverlap(self, arr):
		n = len(arr)
		i = 0
		arr.sort()

		while i < n - 1:
			if arr[i][1] > arr[i + 1][0] and arr[i][1] > arr[i + 1][1]:
				arr.pop(i + 1)
				n -= 1
		elif arr[i][1] >= arr[i + 1][0]:
		arr[i] = [arr[i][0], arr[i + 1][1]]
		arr.pop(i + 1)
		n -= 1

	else:
	i += 1


return arr

ruNmiw - 5j
edge
ruNmiw - 5j
edge
# {
# Driver Code Starts
if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		n = int(input())
		# a = list(map(int, input().strip().split()))
		arr = []
		# j = 0
		for i in range(n):
			a = list(map(int, input().strip().split()))
			x = a[0]
			# j += 1
			y = a[1]
			# j += 1
			arr.append([x, y])
		obj = Solution()
		ans = obj.mergeOverlap(arr)
		for i in ans:
			for j in i:
				print(j, end=" ")
		print()

# } Driver Code Ends

# ⎬coded by⎨ ⌘‣ Mr. Mudgal
