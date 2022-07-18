import math

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1),len(num2))
        num1_pad = num1.zfill(max_len)
        num2_pad = num2.zfill(max_len)
        carry_over = False
        answer = ""
        # print(num1_pad)
        # print(num2_pad)
        for i in range(0,max_len):
            # print("====")
            temp_sum = int(num1_pad[max_len-i-1]) + int(num2_pad[max_len-i-1])
            # print(temp_sum)
            if carry_over:
                temp_sum+=1
            temp_answer = temp_sum % 10
            # print("modulo",temp_answer)
            carry_over = temp_sum > 9
            answer = str(temp_answer) + answer
            # print(answer)
            # print("----")
        return answer



if __name__ == '__main__':
    print(Solution().addStrings("6994","36"))