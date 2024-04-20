# The code you provided implements the Sliding Window technique to find the smallest subarray (or contiguous sublist) 
# of an array `nums` whose sum is greater than or equal to a given `target` value. 

# Here's a breakdown of what's happening:

# Here's a point-wise explanation of the `sliding_window_pattern` function:

# 1. Initialize `wStart` (window start index) and `wSum` (running sum of the window) to 0.
# 2. Initialize `wLength` (length of the smallest subarray found so far) to a large value.
# 3. Check if the `target` sum is greater than the total sum of the array. If so, return "Not Possible".
# 4. Iterate through the array with `wEnd` (window end index):
#    - Add the current element `nums[wEnd]` to `wSum`.
#    - While `wSum` is greater than or equal to the `target`:
#      - Calculate the current window length `curr_window_length = wEnd - wStart + 1`.
#      - Update `wLength` with the minimum of `wLength` and `curr_window_length`.
#      - Subtract the element at `wStart` from `wSum`.
#      - Increment `wStart` to slide the window forward.
# 5. After the loop, return `wLength` (the length of the smallest subarray whose sum is greater than or equal to the `target`).


def sliding_window_pattern(nums, target):
    wStart = 0
    wSum = 0
    wLength = 1e5
    if target > sum(nums):
        return "Not Possible"
    for wEnd in range(len(nums)):
        wSum += nums[wEnd]
        while wSum >= target:
            curr_window_length = wEnd - wStart + 1
            wLength = min(wLength, curr_window_length)
            wSum -= nums[wStart]
            wStart += 1

    return wLength


if __name__ == "__main__":
    # nums= [1,1,1,1,1,1,1,1]
    # target = 11
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    ans = sliding_window_pattern(nums, target)
    print(ans)


