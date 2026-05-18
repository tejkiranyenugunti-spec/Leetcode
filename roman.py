class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i + 1]]:
                ans -= values[s[i]]
            else:
                ans += values[s[i]]

        ans += values[s[-1]]

        return ans

obj = Solution()

print(obj.romanToInt("III"))      
print(obj.romanToInt("LVIII"))    
print(obj.romanToInt("MCMXCIV"))  
## roman to integer
#LC3
#I used a dictionary to keep the Roman numbers and their integer values. I went through the string, and checked the current number against the next number. If the current value was smaller than the next one, then I went for subtractiing it annd then checking and returnign vslue
