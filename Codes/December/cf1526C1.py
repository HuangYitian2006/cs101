import heapq

n=int(input())
potion=list(map(int,input().split()))
h=0
drunk=[]
for i in range(n):
    h+=potion[i]
    heapq.heappush(drunk,potion[i])
    if h<0:
        h-=heapq.heappop(drunk)
    #print(drunk,h)
print(len(drunk))
