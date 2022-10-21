
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a_a = MonthDay(arriveAlice)
        l_a = MonthDay(leaveAlice)
        a_b = MonthDay(arriveBob)
        l_b = MonthDay(leaveBob)
        if a_a.gt(l_b) or a_b.gt(l_a):
            return 0
        elif not (a_a.gt(a_b)) and l_b.gt(l_a):
            return l_a.minus(a_b) + 1
        elif not (a_a.gt(a_a)) and not (l_b.gt(l_a)):
            return l_b.minus(a_b) + 1
        elif not(a_b.gt(a_a)) and l_a.gt(l_b):
            return l_b.minus(a_a) + 1
        elif not(a_b.gt(a_a)) and not (l_a.gt(l_b)):
            return l_a.minus(a_a) + 1




class MonthDay:
    def __init__(self, mm_dd=None):
        splitted = mm_dd.split("-")
        self.month = int(splitted[0])
        self.day = int(splitted[1])

    def gt(self, other):
        if self.month > other.month:
            return True
        elif self.month < other.month:
            return False
        else:
            return self.day > other.day

    def to_num(self):
        result = 0
        for i in range(self.month-1):
            result += num_of_days[i]
        result += self.day
        return result

    def minus(self, other):
        self_num = self.to_num()
        other_num = other.to_num()
        return self_num - other_num

if __name__ == '__main__':
    # test = MonthDay("01-30")
    # test2 = MonthDay("02-01")
    # test3 = MonthDay("01-2")
    # test4 = MonthDay("03-14")
    # # print(test.gt(test3))
    # # print(test.gt(test2))
    # # print(test2.gt(test3))
    # print(test.to_num())
    # print(test2.to_num())
    # print(test3.to_num())
    # print(test4.to_num())
    # print(test2.minus(test))
    print(Solution().countDaysTogether("08-15","08-18","08-16","08-19"))
    print(Solution().countDaysTogether("10-01","10-31","11-01","12-31"))
    print(Solution().countDaysTogether("09-01","10-19","06-19","10-20"))