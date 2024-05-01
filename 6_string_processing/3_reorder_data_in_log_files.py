from pip._vendor.typing_extensions import List


class Solution63:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_dict = {}

        for log in logs:
            words = log.split()

            if words[1].isdigit():
                digit_logs.append(" ".join(words))
            else:
                identifier, content = words[0], " ".join(words[1:])
                letter_dict[(content, identifier)] = log

        # sort_list = [t[0] + " " + t[1] for t in sorted(letter_dict.items(), key=lambda x:(x[1],x[0]))]

        return [log for (_, _), log in sorted(letter_dict.items())] + digit_logs


s = Solution63()
# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(s.reorderLogFiles(logs1))
# ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
logs2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
print(s.reorderLogFiles(logs2))
