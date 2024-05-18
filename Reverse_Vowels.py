#USING QUEUE
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a list of vowel characters, both lowercase and uppercase.
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        # Initialize an empty list to hold the vowels found in the string.
        vowels_list = []
        
        # Initialize an empty string to build the final result.
        reversed_str = ''

        # First loop: iterate over each character in the input string.
        for i in s:
            # Check if the character is a vowel by seeing if it's in the vowels list.
            if i in vowels:
                # If it's a vowel, append it to the vowels_list.
                vowels_list.append(i)

        # Second loop: iterate over each character in the input string again.
        for j in s:
            # Check again if the character is a vowel.
            if j in vowels:
                # If it is a vowel, add the last vowel from vowels_list to the reversed_str.
                # This effectively reverses the order of vowels because we're popping from the end of the list.
                reversed_str = reversed_str + vowels_list.pop()
            else:
                # If it's not a vowel, just add the current character to the reversed_str as is.
                reversed_str = reversed_str + j

        # Return the string that has vowels reversed.
        return reversed_str




#USING 2 POINTERS
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a set of vowels for quick lookup. Using a set optimizes the membership test to O(1) on average.
        vowels = set('aeiouAEIOU')  
        # Convert the immutable string to a list because strings in Python are immutable,
        # and converting it to a list allows for in-place modifications.
        s = list(s)  
        # Initialize two pointers, one starting from the beginning (l) and one from the end (r) of the list.
        l, r = 0, len(s) - 1  
        
        while l < r:  # Continue looping until the two pointers meet or cross each other.
            # Move the left pointer to the right as long as it points to a non-vowel and has not crossed the right pointer.
            while l < r and s[l] not in vowels:
                l += 1
            # Move the right pointer to the left as long as it points to a non-vowel and has not crossed the left pointer.
            while r > l and s[r] not in vowels:
                r -= 1
            
            # Once both pointers point to vowels, swap the vowels at these pointers.
            s[l], s[r] = s[r], s[l]
            
            # After swapping, move both pointers inward to continue the process on the next set of vowels.
            l += 1
            r -= 1

        # Join the list of characters back into a string and return the modified string with vowels reversed.
        return ''.join(s)  


