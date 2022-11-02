主要适用 原始数组不变，频繁查询数组内某个区间的和

- self.presum = [0]*(N+1) 初始化数组
self.presum = [0 for _ in range(n)] 
- 初始化 2-dimension 数组
```python
        # 这样初始化是不行的 
        # self.presum=[[0]*len_col]*len_row
        self.presum = [[0] * (len_col + 1) for _ in range(len_row + 1)]
```