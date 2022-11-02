# 输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# 输出: [-2,0,3,5,3]
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        # init a diff
        diff=[0 for _ in range(length)]

        # diff increment
        for update in updates:
            start,stop=update[0],update[1]
            diff[start]+=update[2]
            if stop+1 < length:
                diff[stop+1]-=update[2]

        # cal res by iterate diff

        res=[0 for _ in range(length)]
        res[0]=diff[0]
        for i in range(1,length):
            res[i]=res[i-1]+diff[i]

        return res



