#USING SPLIT AND JOIN
class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string 's' into a list of words.
        # The split() method by default splits the string by any whitespace and removes extra whitespace.
        x = s.split()
        
        # Reverse the list of words.
        # x[::-1] creates a new list that is a reverse of 'x'.
        # The slicing operation [::-1] is used here to reverse the elements of the list.
        
        # Join the reversed list of words back into a single string with spaces between them.
        # The " ".join() method concatenates the elements of the list 'x[::-1]',
        # inserting a space character between each element to form the final string.
        return " ".join(x[::-1])



#WITHOUT USING SPLIT
class Solution:
    def reverseWords(self, s: str) -> str:
        # Initialize variables
        words = []
        length = len(s)
        i = 0
        
        # Iterate through the string to find and collect words
        while i < length:
            # Skip any leading spaces
            while i < length and s[i] == ' ':
                i += 1
            # At this point, 'i' is at the start of a word
            start = i
            # Continue until the end of the word
            while i < length and s[i] != ' ':
                i += 1
            # Append the word found to the 'words' list
            if start < i:  # Ensure there's at least one character in the current word
                words.append(s[start:i])
        
        # Join and return the reversed list of words
        return ' '.join(reversed(words))

