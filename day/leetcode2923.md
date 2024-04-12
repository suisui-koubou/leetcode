
## 哈希

```python 
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue 
                if grid[i][j]:
                    f[j].add(i)
                else:
                    f[i].add(j)
        return next((index for index, item in enumerate(f) if len(item) == 0), None)
```

- `(index for index, item in enumerate(f) if len(item) == 0)` 可以创建一个 tuple (可迭代，但注意list不可迭代)
- `next(iter, None)` 表示返回 iterator 下一个元素，如果为空，返回 None 默认值。

这里纯属只是语法知识点(绣花功夫)。

### 列表表达式

可以很方便地构造列表，比如 10 内的奇数列表。

```python
l = [i for i in range(10) if i % 2]
```

输出 `[1, 3, 5, 7, 9]`

进阶是100内的平方数

```python 
l = [i*i for i in range(10)]
```

输出 `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

### 生成器表达式

列表表达式不仅可以用于列表，还可以用于元组等其他可迭代对象。

**但是，列表表达式本身生成的是列表，而不是元组或其他类型。如果需要从生成器表达式创建列表，可以使用list()函数。**

```python 
tuple1 = (i * i for i in range(10))  # 生成器表达式
list6 = list(tuple1)  # 将生成器表达式转换为列表
print(list6)  # 输出生成的列表
```

## 每行求和

仔细观察矩阵，可以发现每一行是一队的胜负情况，当一行的和为 `n-1` 时，证明打赢了除了自己以外的所有队伍。

```python 
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, line in enumerate(grid):
            if sum(line) == n - 1: 
                return i 
        return -1 
```

