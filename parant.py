class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        stack = [("", 0, 0)]
        result = []

        while stack:
            s, open_p, close_p = stack.pop()

            if len(s) == 2 * n:
                result.append(s)
                continue

            if open_p < n:
                stack.append((s + "(", open_p + 1, close_p))
            if close_p < open_p:
                stack.append((s + ")", open_p, close_p + 1))

        return result
    
    # I solved this problem using stack-based backtracking. I initialized a stack with an empty string and counters for open and close parentheses. While the stack is not empty, I pop the top element and check if the length of the string is equal to 2 * n. If it is, I add the string to the result list. Otherwise, I check if I can add an open parenthesis (if open_p < n) or a close parenthesis (if close_p < open_p) and push the new state onto the stack. Finally, I return the result list containing all valid combinations of parentheses.