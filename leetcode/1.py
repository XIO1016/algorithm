from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()
        while left < right:
            tmp = arr[left][0] + arr[right][0]
            if tmp == target:
                return [arr[left][1], arr[right][1]]
            elif tmp < target:
                left += 1
            else:
                right -= 1
