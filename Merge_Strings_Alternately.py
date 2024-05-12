class Solution:
    # Define the function to merge two strings alternately.
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Initialize an empty string to store the result.
        result = ''

        # Iterate over the length of the shorter word to ensure each character is used alternately.
        for i in range(min(len(word1),len(word2))):

            # Add one character from each word to the result string in each iteration.
            result = result + word1[i] + word2[i]



        # After finishing the loop, one of the words may still have remaining characters.
        # Check which word is longer and append the rest of its characters to the result.
        if len(word1) > len(word2):
            # If word1 is longer, append the remaining part of word1 to the result.
            result = result + word1[i+1:]
        else:
            # If word2 is longer, append the remaining part of word2 to the result.
            result = result + word2[i+1:]

        # Return the final merged string.
        return result