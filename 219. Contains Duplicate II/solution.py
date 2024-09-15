class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visit = {}
        duplicate, distance = False, False
    
        for i in range(len(nums)):
            if nums[i] not in visit:
                visit[nums[i]] = i
            else:
                duplicate = True

                if i - visit[nums[i]] <= k:
                    distance = True
                    return duplicate and distance
                else:
                    visit[nums[i]] = i

        return False
                ## Store the nearest location that a value appeard
                ## So we should use a hashmap, store (value, id)
            
