class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # init diff
        diff = [0 for _ in range(1001)]

        # cal diff incement
        for trip in trips:
            start,stop=trip[1],trip[2]-1
            diff[start]+=trip[0]

            if stop+1<1001:
                diff[stop+1]-=trip[0]

                if trip[0]>capacity:
                    return False

        
        # cal res
        res = [0 for _ in range(1001)]
        res[0]=diff[0]
        for i in range(1,1001):

            res[i]=res[i-1]+diff[i]
            if res[i]>capacity: 
                return False

        return True

        
