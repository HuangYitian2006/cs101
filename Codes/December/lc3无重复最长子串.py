class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        l,r,mx=0,1,1
        #enumerate(s)
        while r<len(s):
            #print(l,r)
            if s[r] not in s[l:r]:
                r+=1
            else:
                mx=max(mx,r-l)
                l+=s[l:r].index(s[r])+1
                r+=1
        mx = max(mx, r - l)
        return mx


if  __name__=='__main__':
    sol=Solution()
    print(sol.lengthOfLongestSubstring(''))