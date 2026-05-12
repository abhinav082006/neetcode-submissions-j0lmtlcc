class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis_arr = []
        for p in points:
            x = p[0]
            y = p[1]
            dis = math.sqrt((x**2)+(y**2))
            dis_arr.append([dis,[x,y]])
        dis_arr.sort()
        res = []
        for i in range(k):
            res.append(dis_arr[i][1])
        return res
        