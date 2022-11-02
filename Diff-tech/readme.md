- 遍历二维数组
for update in updates: 

- 一些不从 0 计数的数组，需要特殊处理 -1 以满足 index 从 0 开始的输出
start,stop=booking[0]-1,booking[1]-1 

- 差分基础结构

```python
    for update in updates:
        start,stop=update[0],update[1]
        diff[start]+=update[2]
        if stop+1 < length:
            diff[stop+1]-=update[2]
```
