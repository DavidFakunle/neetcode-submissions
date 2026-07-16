class Solution:
    def isValid(self, s: str) -> bool:
        stack= [] # last in, first out, stores opening brackets

        pairs = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
        }

        for char in s:
            if char not in pairs: # checks for opening brakcet 
                stack.append(char) # appending the opening brakcet to stack
            #Case 2: closing bracket
            else: 
                if not stack: # if nothing to match 
                    return False

                top = stack.pop() # get last opening bracket

                if top != pairs[char]:
                    return False

        return len(stack) == 0 # checks if nothing is left 
