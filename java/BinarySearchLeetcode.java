/*
 * @lc app=leetcode id=704 lang=java
 *
 * [704] Binary Search
 */

// @lc code=start
// class BinarySearchLeetcode {
public int search(int[] nums, int target) {
    int pivot, left = 0, right = nums.length - 1;
    while (left <= right) {
        pivot = left + (right - left) / 2;
        if (nums[pivot] == target) return pivot;
        if (target < nums[pivot]) right = pivot - 1;
        else left = pivot + 1;
    }
    return -1;
}
// }

// @lc code=end
