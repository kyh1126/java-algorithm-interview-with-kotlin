import re
from pip._vendor.typing_extensions import List


class Solution64:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        target_list = re.findall("[\dA-Za-z]*", paragraph.lower())
        count_dict = {}

        for target in target_list:
            if target in banned or not target:
                continue
            count_dict[target] = count_dict.get(target, 0) + 1

        # return [k for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse = True)][0]
        return max(count_dict, key=count_dict.get)


s = Solution64()
# "ball"
paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned1 = ["hit"]
print(s.mostCommonWord(paragraph1, banned1))
# "a"
paragraph2 = "a."
banned2 = []
print(s.mostCommonWord(paragraph2, banned2))
