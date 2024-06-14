import random

class Solution1:
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
    
class Solution2:
    def kClosest(self, points, k):
        def partition(l, r, pivot_idx):
            pivot = points[pivot_idx][0]**2 + points[pivot_idx][1]**2
            stored_pivot_idx = l
            
            points[pivot_idx], points[r] = points[r], points[pivot_idx]
            
            for i in range(l, r):
                if (points[i][0]**2 + points[i][1]**2) < pivot:
                    points[stored_pivot_idx], points[i] = points[i], points[stored_pivot_idx]
                    stored_pivot_idx += 1
            
            points[stored_pivot_idx], points[r] = points[r], points[stored_pivot_idx]
            return stored_pivot_idx
        
        def select(l, r, k):
            if l < r:
                pivot_idx = random.randint(l, r)
                pivot_idx = partition(l, r, pivot_idx)
                
                if pivot_idx == k:
                    return
                
                if pivot_idx < k:
                    select(pivot_idx + 1, r, k)
                else:
                    select(l, pivot_idx - 1, k)
                    
        select(0, len(points) - 1, k)
        return points[:k]
    
# Testing 1
test1Instance = Solution1()
points = [[1, 3], [-2, 2]]
k = 1
print(test1Instance.kClosest(points=points, k=k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(test1Instance.kClosest(points=points, k=k))

# Testing 2
test2Instance = Solution2()
points = [[1, 3], [-2, 2]]
k = 1
print(test2Instance.kClosest(points=points, k=k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(test2Instance.kClosest(points=points, k=k))

