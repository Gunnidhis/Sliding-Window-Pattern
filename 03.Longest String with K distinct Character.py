# The code you provided is implementing the Sliding Window technique to find the length of
# the longest substring in a given string `s` that has at most ( maximum ) `k` distinct characters.

# Here's a short explanation of what's happening:

# 1. Initialize `wStart` (the start of the window), `max_length` (to store the length of the longest substring), and `dictionary` (to keep track of the characters and their frequencies).
# 2. Check for edge cases (empty string, `k` greater than string length).
# 3. Iterate through the string with `wEnd` (the end of the window):
#    - Add the character at `wEnd` to the `dictionary` and update its frequency.
#    - If the number of distinct characters is equal to `k`, update `max_length`.
#    - While the number of distinct characters is greater than `k`:
#      - Remove the character at `wStart` from the `dictionary` by decrementing its frequency.
#      - If the frequency becomes zero, remove the character from the `dictionary`.
#      - Increment `wStart` to slide the window.
# 4. Return `max_length` (the length of the longest substring with at most `k` distinct characters).



# The Sliding Window technique is used to maintain a window of characters in the string, and the window is 
# adjusted based on the condition of having at most `k` distinct characters. The `dictionary` is used to keep
# track of the characters and their frequencies within the current window.



def longest_string_with_distinct_character(s, k):
    # we have return longest string length with k distinct character
    wStart = 0
    max_length = -1
    dictionary = dict()
    if s == None or k > len(s) or len(s) == 0:
        return max_length

    for wEnd in range(len(s)):
        rightChar = s[wEnd]
        if rightChar not in dictionary:
            dictionary[rightChar] = 0
        dictionary[rightChar] += 1

        if len(dictionary) == k:
            max_length = max(max_length, wEnd - wStart + 1)

        while len(dictionary) > k:
            leftchar = s[wStart]
            dictionary[leftchar] -= 1
            if dictionary[leftchar] == 0:
                del dictionary[leftchar]
            wStart += 1

    return max_length


if __name__ == "__main__":
    s = "araaci"
    k = 2
    ans = longest_string_with_distinct_character(s, k)
    print(ans)

#The example usage finds the length of the longest substring with at most 2 distinct characters in the string "araaci", which is 4 (the substring "araa").
