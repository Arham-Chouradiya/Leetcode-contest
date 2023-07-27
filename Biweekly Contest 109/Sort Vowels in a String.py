class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        stack = []
        for ch in s:
            if ch in "aeiouAEIUO":
                stack.append(ch)
        stack.sort()
        stack=stack[::-1]
        for i in range(len(s)):
            if s[i] in "aeiuoAEOUI":
                s[i] = stack[-1]
                stack.pop()
        return "".join(s)