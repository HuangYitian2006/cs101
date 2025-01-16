class Solution(object):
    def spiralOrder(self, matrix):
        l,r,t,b,ans=0,len(matrix[0])-1,0,len(matrix)-1,[]
        while t<=b and l<=r:
            for i in range(l,r+1):
                ans.append(matrix[t][i])
            t+=1
            if t>b:break
            for i in range(t,b+1):
                ans.append(matrix[i][r])
            r-=1
            if r < l: break
            for i in range(r,l-1,-1):
                ans.append(matrix[b][i])
            b-=1
            if t > b: break
            for i in range(b,t-1,-1):
                ans.append((matrix[i][l]))
            l+=1
            if r < l: break
        return ans

if __name__=='__main__':
    a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    sol=Solution()
    print(sol.spiralOrder(a))