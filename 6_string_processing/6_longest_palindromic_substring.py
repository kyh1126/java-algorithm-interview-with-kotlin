class Solution66:
    def extendPalindrome(self, s: str, j: int, k: int) -> None:
        # 투 포인터가 유효한 범위 내에 있고 양쪽 끝 문자가 일치하는 팰린드롬인 경우 범위 확장
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1

        # 기존 최대 길이보다 큰 경우 값 교체
        if self.maxLen < k - j - 1:
            self.left = j + 1
            self.maxLen = k - j - 1

    def longestPalindrome(self, s: str) -> str:
        # 문자 길이 저장
        length = len(s)

        # 길이가 1인 경우 예외 처리
        if length < 2:
            return s

        # 초기화
        self.left = 0
        self.maxLen = 0

        # 우측으로 한 칸씩 이동하며 투 포인터 조사
        for i in range(length - 1):
            self.extendPalindrome(s, i, i + 1)  # 2칸짜리 투 포인터
            self.extendPalindrome(s, i, i + 2)  # 3칸짜리 투 포인터

        # 왼쪽과 최대 길이만큼을 더한 오른쪽만큼의 문자를 정답으로 리턴
        return s[self.left:self.left + self.maxLen]


s = Solution66()
# "bab"
s1 = "babad"
print(s.longestPalindrome(s1))
# "bb"
s2 = "cbbd"
print(s.longestPalindrome(s2))
