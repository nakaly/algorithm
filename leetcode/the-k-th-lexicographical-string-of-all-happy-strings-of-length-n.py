



class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        happyString(['a','b','c'],"","",n, result)
        return result[k-1]



def happyString(alphabet,happy, prev, n, result):
    if len(happy) == n:
        return happy
    for c in alphabet:
        if c != prev:
            ok = happyString(alphabet, happy+c, c, n, result)
            if ok is not None and len(ok) == n:
                result.append(ok)


if __name__ == '__main__':
    print(Solution().getHappyString(3,9))