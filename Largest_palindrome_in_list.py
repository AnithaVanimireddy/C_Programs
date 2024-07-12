def is_palindrome(s):
    return s == s[::-1]
def largest_palindrome(lst):
    largest = ""
    for s in lst:
        if is_palindrome(s) and len(s) > len(largest):
            largest = s
    return largest
data = ["madam", "racecar", "hello", "level", "world", "noon"]
largest_pal = largest_palindrome(data)
print("Largest palindrome is:", largest_pal)
