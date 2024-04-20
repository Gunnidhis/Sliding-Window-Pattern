# This code is implementing the Sliding Window technique to find the length of the longest 
# substring without repeating characters in a given string `s`.

# Here's a short explanation:

# 1. Initialize `wStart` (start of the window), `max_length` (to store the maximum length),
# and `dic` (dictionary to store character positions).
# 2. Check if the string is empty, and return 0 if it is.
# 3. Iterate through the string with `wEnd` (end of the window):
#    - Get the current character `curr_char`.
#    - If `curr_char` is in the dictionary:
#      - Update `wStart` to the position after the previous occurrence of `curr_char`.
#    - Update `max_length` with the maximum of `max_length` and the length of the current
#      window (`wEnd - wStart + 1`).
#    - Store the position of `curr_char` in the dictionary.
# 4. Return `max_length` (the length of the longest substring without repeating characters).



#The Sliding Window technique is used to maintain a window of unique characters in the string. The dictionary 
#`dic` is used to keep track of the positions of characters within the current window. If a character is encountered 
#that already exists in the window, the start of the window (`wStart`) is moved to the position after the previous 
#occurrence of that character, effectively shrinking the window to exclude the repeated character.

def longest_string_without_repeating_character(s):
    wStart = 0
    max_length = -1
    dic = dict()
    if s == "":
        return 0
    for wEnd in range(len(s)):
        curr_char = s[wEnd]
        if curr_char in dic:
            wStart = max(wStart, dic[curr_char] + 1)
        max_length = max(max_length, wEnd - wStart + 1)
        dic[curr_char] = wEnd
    return max_length


if __name__ == "__main__":
    string = "abcabcbb"
    max_length = longest_string_without_repeating_character(string)
    print(max_length)
