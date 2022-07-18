

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        phrases = s.split("-")
        license_string = "".join(phrases).upper()
        length = len(license_string)
        first = length % k
        num_of_blocks = int((length - first) / k)
        answer = ""
        if num_of_blocks <= 0:
            return answer
        start = 0
        if first == 0:
            answer = license_string[0:k]
            num_of_blocks -=1
            start = 1
        else:
            answer = license_string[0:first]
        for i in range(0, num_of_blocks):
            answer = answer + "-" + license_string[(i+start)*k+first:(i+start+1)*k+first]
        return answer



if __name__ == '__main__':
    print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))