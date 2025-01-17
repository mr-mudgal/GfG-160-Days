class Solution:
    def compute_lps(self, concat):
        n = len(concat)
        lps = [0] * n
        length = 0
        i = 1
    
        while i < n:
            if concat[i] == concat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
    
        return lps
    
    def minChar(self, s):
        concat = s + '#' + s[::-1]
        lps = self.compute_lps(concat)
        return len(s) - lps[-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends

# ⎬coded by⎨ ⌘‣ Mr. Mudgal
