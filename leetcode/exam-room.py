import heapq


class ExamRoom:

    def __init__(self, n: int):
        self.q = []
        self.s = set()
        self.n = n

    def seat(self) -> int:
        if len(self.s) == 0:
            heapq.heappush(self.q, 0)
            self.s.add(0)
            return 0
        else:
            low = 0
            high = self.n - 1
            cur = 0
            diff = 0
            l = []
            prev_dis = 0
            if 0 not in self.s:
                l.append(0)
            l.extend(sorted(self.q))
            if high not in self.s:
                l.append(high)
            for item in l:
                tmp_diff = item - cur
                if diff+1 < tmp_diff:
                    low = cur
                    high = item
                    diff = tmp_diff
                cur = item
            if low not in self.s:
                found = low
            elif high not in self.s:
                found = high
            else:
                found = (high + low) // 2

            heapq.heappush(self.q, found)
            self.s.add(found)
            return found

    def leave(self, p: int) -> None:
        self.q.remove(p)
        self.s.remove(p)


if __name__ == '__main__':
    obj = ExamRoom(10)
    commands = ["seat", "seat", "seat", "seat", "leave", "seat"]
    params = [[], [], [], [], [4], []]
    result = []
    for i in range(len(commands)):
        if commands[i] == "seat":
            result.append(obj.seat())
        else:
            obj.leave(params[i][0])
            result.append(None)

    print(result)
