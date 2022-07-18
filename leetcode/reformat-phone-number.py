
class Solution:
    def reformatNumber(self, number: str) -> str:
        replaced = number.replace(" ","").replace("-","")

        len_of_num = len(replaced)
        mod_3 = len_of_num % 3
        answer = ""
        index = 0
        if mod_3 == 0:

            while index < len_of_num:
                answer += replaced[index:index+3]
                index += 3
                if index < len_of_num:
                    answer += "-"
            return answer
        elif mod_3 == 1:
            while index + 5 < len_of_num:
                answer += replaced[index:index+3]
                index += 3
                answer += "-"
            answer += replaced[index:index+2] + "-" + replaced[index+2:index+4]
            return answer
        else:
            while index + 2 < len_of_num:
                answer += replaced[index:index+3]
                index += 3
                answer += "-"
            answer += replaced[index::]
            return answer

if __name__ == '__main__':
    print(Solution().reformatNumber("123 4-5678"))