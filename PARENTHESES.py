def is_valid(s):
    stack = []
    match = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in match:
            if not stack or stack.pop() != match[ch]:
                return False
        else:
            stack.append(ch)

    return len(stack) == 0


s = "()[]{}"
print(is_valid(s))

# I used a stack to push and pop the parentheses. I added brackets to the stack, for every closing bracket I checked if the top of the stack is according to the match and  if not then I retuned False.