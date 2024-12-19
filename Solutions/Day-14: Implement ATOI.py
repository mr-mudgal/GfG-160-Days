#User function template for Python
class Solution:
    def myAtoi(self, s):
        s = s.strip()
        s = s.lstrip('0')
        if not len(s):
            return 0
        s = s[::-1]

        integer = 0
        factor = 1

        for i in s:
            if i.isnumeric():
                integer += int(i) * factor
                factor *= 10
            elif i.isalpha():
                integer = 0
                factor = 1
        
        if s[-1] == '-':
            integer = 0 - integer
        
        if integer >= 2**31 - 1:
            integer = 2147483647
        elif integer <= -2**31:
            integer = -2147483648

        return integer
                

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends

# ⎬coded by⎨ ⌘‣ Mr. Mudgal
