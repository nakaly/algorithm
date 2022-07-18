

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        index = 0
        for c in key.replace(" ", ""):
            if not c in decode:
                decode[c] = alphabet[index]
                index += 1
                if index == 26:
                    break

        return "".join(decode[c] if c != ' '  else ' ' for c in message)



if __name__ == '__main__':
    print(Solution().decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))

