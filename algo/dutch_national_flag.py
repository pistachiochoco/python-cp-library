"""
Dutch National Flag Algorithm (by Edsger Dijkstra)

Sort an array with 0, 1, 2 in-place.

Time Complexity: O(n)
Space Complexity: O(1)

Example problem: https://leetcode.com/problems/sort-colors
"""

from typing import List


def dutch_national_flag(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    

if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    dutch_national_flag(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]