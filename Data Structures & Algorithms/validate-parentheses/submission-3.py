class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(', '{', '['}
        for char in s:
            if char in opening:
                stack.append(char)
            elif len(stack) == 0: return False
            elif char == ')' and stack.pop() != '(': return False
            elif char == '}' and stack.pop() != '{': return False
            elif char == ']' and stack.pop() != '[': return False
        return len(stack) == 0