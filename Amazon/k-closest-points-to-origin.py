class Solution:
    def kClosest(self, points, k):
        def calc_distance(x, y):
            return abs(x)**2 + abs(y)**2

        def sort_with_distance(point):
            distance_idx = 0
            return point[distance_idx]

        distance_with_point = []
        for point in points:
            x, y = 0, 1
            distance = calc_distance(point[x], point[y])
            distance_with_point.append([distance, point])

        distance_with_point.sort(key=sort_with_distance)

        result = []
        for i in range(k):
            result.append(distance_with_point[i][1])

        return result
    
# Testing
testInstance = Solution()
points = [[1, 3], [-2, 2]]
k = 1
print(testInstance.kClosest(points=points, k=k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(testInstance.kClosest(points=points, k=k))