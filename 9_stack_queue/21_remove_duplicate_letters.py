class Solution921:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {}
        seen = set()
        stack = []

        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        for c in s:
            counter[c] -= 1

            if c in seen:
                continue

            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return ''.join(stack)


s = Solution921()
# "abc"
s1 = "bcabc"
print(s.removeDuplicateLetters(s1))
# acdb
s2 = "cbacdcbc"
print(s.removeDuplicateLetters(s2))
