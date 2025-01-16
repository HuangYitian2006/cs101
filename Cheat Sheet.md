# Cheat Sheet

### 常用函数

```python
#list
a=[]
a.append('x')
a.pop()
a.extend([x,y,z])

#set
a=set()
a.add()

#dic
a=dict()
a[keyx]=valuex

#deque
from collections import deque
a=deque()
a.append(x)
a.appendleft(x)
a.pop()
a.popleft()

#heapq 优先队列or堆
import heapq
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heapq.heapify(data)
print(data) # 输出: [0, 1, 2, 3, 9, 5, 4, 6, 8, 7]

heapq.heappush(data, -5)
print(data) # 输出: [-5, 0, 2, 3, 1, 5, 4, 6, 8, 7, 9]
print(heapq.heappop(data)) # 输出: -5

```

### 深拷贝

```
#深拷贝 复制数组时用！
import copy
original = [1, 2, [3, 4]]
copied = copy.deepcopy(original)
print(copied) # 输出: [1, 2, [3, 4]]
```

