# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def max_Consicutive_ones(nums, k):
    ones = 0
    maxlen = 0
    wStart = 0
    for wEnd in range(len(nums)):
        curr = nums[wEnd]
        if curr == 1:
            ones += 1

        # we can also count 'Zero' but it's my pattern to solve the problem is that we should maintain the data of that variable which we want to maintain
        # In this question our main goal to maximise the occurance of '1' so i maintain the count of '1'.
      
        # number of zeros in window = window length - number of ones in window
        if (wEnd - wStart + 1 - ones) > k:
            if nums[wStart] == 1:
                ones -= 1
            wStart += 1
        maxlen = max(maxlen, wEnd - wStart + 1)
    return maxlen


if __name__ == "__main__":

    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    ans = max_Consicutive_ones(nums, k)
    print(ans)
