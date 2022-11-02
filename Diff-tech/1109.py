class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        # init diff
        diff=[0 for _ in range(n)]

        # diff increment
        for booking in bookings:
            start,stop=booking[0]-1,booking[1]-1
            diff[start]+=booking[2]

            if stop+1<n:
                diff[stop+1]-=booking[2]

        # get res from iterate diff
        res=[0 for _ in range(n)]
     
        for i in range(n):
            res[i]=res[i-1]+diff[i]

        return res