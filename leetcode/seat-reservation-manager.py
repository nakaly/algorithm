import heapq

class SeatManager:
    def __init__(self, n: int):
        self.number_of_seat = n
        self.availableSeats = [i for i in range(n)]
        self.availableSeatsSet = set(self.availableSeats)
        heapq.heapify(self.availableSeats)

    def reserve(self) -> int:
        seat = heapq.heappop(self.availableSeats)
        self.availableSeatsSet.remove(seat)

        return seat + 1

    def unreserve(self, seatNumber: int) -> None:
        index = seatNumber - 1
        if not index in self.availableSeatsSet:
            heapq.heappush(self.availableSeats, index)
            self.availableSeatsSet.add(index)


if __name__ == '__main__':
    operation = ["SeatManager","reserve","unreserve","reserve","reserve","unreserve","reserve","unreserve","reserve","unreserve","reserve"]
    values = [[2],[],[1],[],[],[2],[],[1],[],[2],[]]


    obj = SeatManager(values[0][0])
    for i, operation in enumerate(operation):
        if operation == "reserve":
            print(obj.reserve())
        elif operation == "unreserve":
            print(obj.unreserve(values[i][0]))
