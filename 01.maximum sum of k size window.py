# Given an array and an integer K, find the maximum for each and every contiguous subarray of size K

# The function finds the maximum sum of a subarray of size `k` in the given array `nums` using the Sliding Window technique.

# 1. Initialize `wStart`, `wSum` (running sum of the window), and `max_sum` (maximum sum found so far).
# 2. Iterate through `nums` with `wEnd`:
#    - Add the current element `nums[wEnd]` to `wSum`.
#    - If the window size is `k`:
#      - Update `max_sum` with the maximum of `max_sum` and `wSum`.
#      - Subtract the element at `wStart` from `wSum`.
#      - Increment `wStart` to slide the window.
# 3. Return `max_sum` (the maximum sum of a subarray of size `k`).

# The example usage finds the maximum sum of a subarray of size 3 in the array `[2, 3, 1, 2, 4, 3]`.

def sliding_window_max_sum(nums, k):
    wStart = 0
    wSum = 0
    max_sum = -1
    for wEnd in range(len(nums)):
        wSum += nums[wEnd]
        if wEnd - wStart + 1 == k:
            max_sum = max(max_sum, wSum)
            wSum -= nums[wStart]
            wStart += 1
    return max_sum


if __name__ == "__main__":
    # nums= [1,1,1,1,1,1,1,1]
    # target = 11
    nums = [2, 3, 1, 2, 4, 3]
    k = 3
    ans = sliding_window_max_sum(nums, k)
    print(ans)
