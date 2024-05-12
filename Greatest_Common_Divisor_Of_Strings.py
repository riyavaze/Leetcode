class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if the concatenation of str1 and str2 is equal to the concatenation of str2 and str1
        # This check is crucial because if str1 and str2 can be decomposed into the same repeating unit,
        # their concatenations in different orders should produce the same string.
        if str1 + str2 != str2 + str1:
            # If they are not the same, it means there is no common repeating string that can divide both,
            # hence return an empty string.
            return ""
        
        # Import the gcd (Greatest Common Divisor) function from the math module
        from math import gcd
        # Printing the gcd of the lengths of str1 and str2 for debugging or understanding the flow.
        print(gcd(len(str1), len(str2)))
        
        # Return the substring from the beginning of str1 up to the length that is the greatest common divisor
        # of the lengths of str1 and str2. This is based on the principle that the greatest common divisor of the
        # lengths will give us the maximum length of the repeating string pattern that can divide both strings.
        return str1[:gcd(len(str1), len(str2))]
    


# WITHOUT USING ANY IMPORTS
class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function that checks if 'potential' can completely divide 's'
        # by repeating 'potential' enough times to exactly match 's'.
        def divides(s, potential):
            # If 'potential' is longer than 's', it cannot divide 's'.
            if len(potential) > len(s):
                return False
            # If the length of 's' is not a multiple of the length of 'potential',
            # 'potential' cannot divide 's' evenly.
            if len(s) % len(potential) != 0:
                return False
            # Calculate how many times 'potential' should be repeated to match the length of 's'.
            multiplier = int(len(s) / len(potential))
            # Check if repeating 'potential' 'multiplier' times equals 's'.
            return potential * multiplier == s

        # Ensure str1 is the shorter string, or equal length, to optimize the search of potentials.
        if len(str2) < len(str1):
            str1, str2 = str2, str1

        # Start checking from the first character up to the length of the shorter string.
        prefixLength = 1
        # This list will store all potential substrings that can divide both strings.
        potentials = []
        while prefixLength <= len(str1):
            # Extract a potential substring from the start up to prefixLength.
            potential = str1[:prefixLength]
            # Check if this 'potential' substring divides both str1 and str2.
            if divides(str1, potential) and divides(str2, potential):
                # If it does, add it to the list of possible solutions.
                potentials.append(potential)
            # Increment to check the next length of potential substring.
            prefixLength += 1
        # If no potentials were found, return an empty string; otherwise, return the longest found.
        # The longest valid string is stored at the end of the potentials list because substrings
        # were checked and stored in increasing length order.
        return "" if len(potentials) == 0 else potentials[-1]
