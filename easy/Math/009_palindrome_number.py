def isPalindromeInt(x):
    if x < 0:
        return False
    if x % 10 == 0 and x != 0:
        return False
    reversed = 0
    while x > reversed:
        last_digit = x % 10
        reversed = reversed*10 + last_digit
        x = x // 10
    return x == reversed or x == reversed // 10 

print(isPalindromeInt(123))
print(isPalindromeInt(1-23))
print(isPalindromeInt(121))