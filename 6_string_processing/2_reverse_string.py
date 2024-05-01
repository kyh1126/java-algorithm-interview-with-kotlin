from pip._vendor.typing_extensions import List


class Solution62:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        while start < end:
            imsi = s[start]
            s[start] = s[end]
            s[end] = imsi

            start += 1
            end -= 1

        print(s)


s = Solution62()
# ["o","l","l","e","h"]
s1 = ["h", "e", "l", "l", "o"]
s.reverseString(s1)
# ["h","a","n","n","a","H"]
s2 = ["H", "a", "n", "n", "a", "h"]
s.reverseString(s2)
