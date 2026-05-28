def longest_palindrome(s):
    res = ""

    for i in range(len(s)):
      
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1

        
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1

    return res


s = "babad"
print(longest_palindrome(s))

s = "cbbd"
print(longest_palindrome(s))

# I checked both odd and even length of the string by using 2 pointers  one in left and  one in right and moved them until both pointers are same. 