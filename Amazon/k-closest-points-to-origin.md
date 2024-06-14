# Topic Area
- [x] Array
- [x] Math
- [x] Divide and Conquer
- [x] Geometry
- [x] Sorting
- [x] Heap (Priority Queue)
- [ ] Quickselect

## Quick Select
Like Quicksort, Quickselect relies on partitioning, and can be thought of as a hybrid of Quicksort and binary search

## Approach used in this problem.
In my approach to solving this question, I used **sorting**

1. Create a new array
2. Store the distance and point in the new array
3. Sort new array based on distance
4. Loop through new array from index 0 to k to get the k closest points, that becomes our final results

Time complexity: O(NlogN)
Memory complexity: O(N)

There is another approach with a reduced time complexity and constant memory using q**uickselect**

- In partition fxn
1. Move pivot to end
2. Now start moving elements less than pivot to left and greater to right
3. Move pivot to the position it is supposed to be in

- In select fxn
1. Generate a pivot_index and call the partition fxn
2. if the pivot index is equal to k return
3. if not but less than k , make a recursive call to select fxn and update left pointer
4. if not but greater than k, make a recursive call to select fxn and update right pointer

Time complexity: O(N), worst could be O(N^2)
Memory complexity: O(1)

```code 
class Solution:
    def kClosest(self, points, k):
        def partition(l, r, pivot_index):
            pivot = points[pivot_index][0]**2 + points[pivot_index][1]**2
            store_index = l

            # moves pivot to end
            points[pivot_index], points[r] = points[r], points[pivot_index]

            # move elements less than pivot to left and vice versa
            for i in range(l, r):
                if (points[i][0]**2 + points[i][1]**2) < pivot:
                    points[store_index], points[i] = points[i], points[store_index]
                    store_index += 1
            
            # swap pivot back to where it is supposed to be after _store_index is updated
            points[store_index], points[r] = points[r], points[store_index]
            return store_index 
        
        def select(l, r, k):
            # select will run only when l < r
            if l < r:
                # generate a random pivot_index between l and r
                pivot_index = random.randint(l, r)
                # update pivot_index until it equals k
                pivot_index = partition(l, r, pivot_index)

                if pivot_index == k:
                    return

                if pivot_index < k:
                    select(pivot_index + 1, r, k)
                else:
                    select(l, pivot_index - 1, k)
                

        select(0, len(points) - 1, k)
        return points[:k]
```