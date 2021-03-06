#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

from typing import List

# @lc code=start

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target: return pivot
        if target < nums[pivot]: right = pivot - 1
        else: left = pivot + 1

    return -1
# @lc code=end
