

from typing import List
import re


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        patterns = re.findall(r'[A-Z][a-z]*', pattern)
        # print(patterns)
        result = []
        for query in queries:
            for pat in patterns:
                all_match = True
                match = re.search('^' + pat + '[a-z]*', query)
                if match is None:
                    all_match = False
                    continue

                query = query[len(match.group(0)):]
                # print(query)
            if all_match and query == '':
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    print(Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))