def longestValidParentheses(s):
    stack = [-1]
    max_len = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            stack.pop()
            if stack == []:
                stack.append(i)
            else:
                lent = i - stack[-1]
                max_len = max(max_len, lent)
    return max_len

print(longestValidParentheses("(()")) 
print(longestValidParentheses("())()(()"))
print(longestValidParentheses(")()())")) 
print(longestValidParentheses(" ")) 