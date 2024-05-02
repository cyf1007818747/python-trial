# "0" => "0"
# "00009": [4, ... , 1] =>.    9
# "000099": [4, ... , 2] => 900..009
# "0000099": [5, ... , 2] => 900.0.009
# "444947137": [0, 1, 0, 1, 4, 0, 0, 2, 0, 1] => 744.9.447

# start to AC - 18:52, with oral explanation and example demonstration
# AC
class Solution:
    def largestPalindromic(self, num: str) -> str:
        # get the frequencies of all digits
        freq = [0] * 10
        for c in num:
            freq[int(c)] += 1

        # for the freq array, iterate from digits 9 to 0:
        # > if freq is even, append after first and before the end of final string for freq //2 times
        # > if is odd, do the same as above and decrease the appended freq, 
        #.  for the remaining 1, insert in the middle if middle is empty, else none
        # edge case: for 0: only insert to start if start nonempty
        # trick: use 3 strings start, middle, end
        start, middle, end = "", "", ""
        for i in range(9, -1, -1):
            while freq[i] >= 2 and (i != 0 or len(start) > 0):
                start += str(i)
                end = str(i) + end
                freq[i] -= 2
            
            if freq[i] >= 1 and middle == "":
                middle = str(i)

        # contact 3 strings
        return start + middle + end

# avoid continuously appending strings, making the solution O(1) complexity
# AC
class Solution:
    def largestPalindromic(self, num: str) -> str:
        # get the frequencies of all digits
        freq = [0] * 10
        for c in num:
            freq[int(c)] += 1

        # for the freq array, iterate from digits 9 to 0:
        # > if freq is even, append after first and before the end of final string for freq //2 times
        # > if is odd, do the same as above and decrease the appended freq, 
        #.  for the remaining 1, insert in the middle if middle is empty, else none
        # edge case: for 0: only insert to start if start nonempty
        # trick: use 3 strings start, middle, end
        start, middle, end = "", "", ""
        for i in range(9, -1, -1):
            # while freq[i] >= 2 and (i != 0 or len(start) > 0):
            #     start += str(i)
            #     end = str(i) + end
            #     freq[i] -= 2
            freq_half = freq[i] // 2
            if freq_half > 0 and (i != 0 or len(start) > 0):
                start += str(i) * freq_half
                end = str(i) * freq_half + end
                freq[i] -= freq_half * 2
            
            if freq[i] >= 1 and middle == "":
                middle = str(i)

        # contact 3 strings
        return start + middle + end
