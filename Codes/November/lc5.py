class Solution(object):
    def longestPalindrome(self, s):
        m=0
        ms=''
        for i in range(len(s)):
            j=0
            while 0<=i-j<=i+j<len(s):
                if s[i-j]==s[i+j]:
                    if 1+j*2>m:
                        m=1+j*2
                        ms=s[i-j:i+j+1]
                else:
                    break
                j+=1
        for i in range(len(s)-1):
            j = 0
            while 0 <= i - j <= i + 1 + j < len(s):
                if s[i - j] == s[i+1+j]:
                    if 2 + j * 2 > m:
                        m = 2 + j * 2
                        ms = s[i - j:i + j + 2]
                else:
                    break
                j += 1
        return ms

if __name__=='__main__':
    sol=Solution()
    print(sol.longestPalindrome("queue"))