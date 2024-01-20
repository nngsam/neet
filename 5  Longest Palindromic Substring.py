# # METHOD1
# def longestPalindrome(s):
#     def check(i,j):
#         """ Check whether the substrings from index i to j-1 is a palindrome """

#         left = i
#         right = j - 1
#         #- start at the given indice and move towards the center, comparing character to determine if they match

#         while left < right:
#             if s[left] != s[right]:
#                 return False #- mismatch, return False
#             left += 1
#             right -= 1

#         return True #- If the pointers meet or cross each other without any mismatches, the function return True, indicating that the substring is a palindrome
    
#     ### MAIN PART, use 2 nested loops to iterate over all possible substrings in the string "s"

#     # Outer loop iterates over the possible lengths of substrings, from the length of the input string "s" down to 1
#     for length in range(len(s), 0, -1): #- iterate from the longest possible length and gradually decreasing
#         # Inner loop interates over the possible starting indices of substrings, ranging from 0 to len(s) - lenth
#         for start in range(len(s) - length + 1):
#             if check(start, start+length):
#                 return s[start:start+length]
            
#     return ""

# print(longestPalindrome('babad'))

# # NOTES:
# #- "length" variable represents the current length of the substrings being checked
# #- For each substrings being checked, the "check()" function is called to determine if if is a palindrome. If the substring is a palindrome, the function returns the substring itself (-return then what next?)
# #- AS we are iterating from the longest possible length down to 1, the first palindrome found will be the longest
# #- If no palindrome string found, an empty string is returned ("")

# # METHOD 2: DYNAMIC PROGRAMMING
# # INTUITION: Let's say we knew the substring with inclusive bounds i,j was a palindrome. If s[i-1] = s[j+1], then we know the substring with inclusive bounds i-1, j+1 must also be a palindrome, and this check can be done in constant time. 
# #- We can flip the direction of this logic as well if s[i] == s[j] and the substrings i+1, j-1 is a palindrome, then the substrings i, j must also be a palindrome
# #- We know that all substring of length 1 are palindromes. From this, we can check if each substrings of length 3 is a palindrome using the above fact. We just need to check every i, j pair where j-i = 2. Once we know all palindromes of length 3, we can use that information to fiind all palindromes of lenth 5, and then 7 and so on
# #- 

# class Solution:
#     def longestPalindrome(self, s):
#         n = len(s)
#         # Create a 2D boolean(T/F) table 'dp' with dimension nxn, store information about whether substrings are palindromes
#         #- Initialize all value to be False
#         dp = [[False] * n for _ in range(n)] 

#         #- Initilize a list 'ans' to store the starting and ending indices of the longest palindrome substring found so far
#         ans = [0,0] #- indicate the empty string

#         for i in range(n):
#             #- Set all diagonal to True, indicating that single characters are palindromes
#             dp[i][i] = True 


#         # This loop
#         #- check for palindrome of length2 by comparing adjacent characters
#         for i in range(n-1):
#             if s[i] == s[i+1]:
#                 dp[i][i+1] = True #- substring from 1_i+1 is a palindrome
#                 ans = [i,i+1] #- update the longest palindrome substring found so far

#         # This nested loop
#         #- Iterate over all possible lengths of palindrome substrings greater than 2
#         #- The outer loop iterates over the difference in indices 'diff', starting from 2 up to 'n-1'
#         #- The inner loop interates over the starting indices 'i' for substrings of the current length
#         #- For each substring, it checks if the characters at indices 'i' and 'j' are the same && if "i+1" and 'j-1' is palindromes
#         #- if both conditions satisfied, indicating that the substring from i to j is a palindrome. It updates the 'ans' to [i,j], indicating the longest palindrome substring found so far

#         for diff in range(2, n):
#             for i in range(n-diff):
#                 j = i+ diff
#                 if s[i] == s[j] and dp[i+1][j-1]:
#                     dp[i][j] = True
#                     ans = [i,j]

#         i,j = ans
#         return s[i:j+1]


# # By starting with palindromes of length 1, then checking for palindromes of length 2, and finally expanding to longer palindromes,
# #- the algorithm gradually builds a dynamic programming table "dp" where each entry dp[i][j] indicates whether the substrings from indix i to j is a palindrome. 
# #- The algorithm keeps track of the longest palindromic substring found so far using the 'ans' list


# Method 3: 
def method3():
    """ In the first approach, the palindrome check cost O(n)
        In the second approach, the palidrome check cost O(1)
        --> This allows us to improve the time complexity from O(n^3) to O(n^2)
        The problem with the second approach is that we always iterated over O(n2) states of i,j 
        --> Can we optimize further to minimize the number of iterations requierd?
        
        The promising solution - we can lower the minimum iterations required if we focus on the centers instead of on the bounds
        """
    pass
#- dist correctly represents the number of characters on each side
class Solution: 
    def longestPalindromes3(self,s):
        def expand(i,j):
            """ Helper function that starts two pointer left, right as a center
            i != j: considering even-length palindromes
            i == j: considering odd-length palindromes
            We will expand from the center (outward) as afar as we can to find the longest palindrome, and then return the length of this palindrome

            Purpose: FIND THE LENGTH OF THE LONGEST PALINDROME CENTERED AT i,j
            """
            
            left = i
            right = j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            #- len(substring) = right - left + 1, start = left, end = right
            #- However, when thel loop ends, it implies, s[left] != s[right]
            #--> need to subtract 2 --> right - left - 1
            return right - left - 1
        
        #- Initialize ans which hold the inclusive bounds of the answer
        ans = [0,0]

        # Iterate i over all indices of s
        for i in range(len(s)):
            odd_length = expand(i,i) #- length of the longest odd-length palindrome centered at i
            if odd_length > ans[1] - ans[0]+1:
                dist = odd_length // 2 #- number of characters on each side
                ans = [i-dist, i+dist]

            even_length = expand(i,i+1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i+1+dist]
        
        i,j = ans #- retrieve the answer bounds "ans" as i,j
        return s[i:j+1] #- return the substrings of s starting at index "i" and ending with index "j"
abc = Solution()

print(abc.longestPalindromes3('babad'))
# Note: puepose of all these code is to find the index of the longthest palindrome substring, then getting the index, return s[index:index]


### METHOD 4: Manacher's Algorithm

