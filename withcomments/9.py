class Solution:
    def isValid(s: str) -> bool:  # Method to check if the string contains valid parentheses
        if len(s) % 2 != 0:  # If the length of the string is odd, it cannot be valid
            return False
        
        mapV = {")": "(", "}": "{", "]": "["}  # Mapping of closing brackets to their corresponding opening brackets
        stackV = []  # Stack to keep track of opening brackets

        for c in s:  # Iterate through each character in the string
            if c in mapV:  # If the character is a closing bracket
                if stackV and stackV[-1] == mapV[c]:  # Check if the stack is not empty and the top matches the corresponding opening bracket
                    stackV.pop()  # Pop the matching opening bracket from the stack
                else:
                    return False  # If no match, the string is invalid
            else:
                stackV.append(c)  # If the character is an opening bracket, push it onto the stack
        
        return True if not stackV else False  # If the stack is empty, all brackets are matched; otherwise, it's invalid

    print(isValid("([]()"))  # Test the function with an example


'''
Summary

    DSA Used: Stack, Dictionary (Hash Map).

    Time Complexity: O(n).

    Space Complexity: O(n).

'''