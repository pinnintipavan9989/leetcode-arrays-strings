def isValid(s):
    stack = []
    bracket_map = {')':'(',']':'[','}':'{'}

    for char in s:
        if char in ('([{'):
            stack.append(char)
        elif char in (')]}'):
            if not stack:
                return False
            if stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False         
    return len(stack) == 0
  
print(isValid(')[]{}'))
print(isValid('())[]{}'))
print(isValid('()[]{}'))