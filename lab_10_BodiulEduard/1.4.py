is_palindrome = lambda s: (clean:= s.lower().replace(' ', '')) == clean[::-1]
print(is_palindrome('Anna'))