
class State:
    def __init__(self, length=0):
        self.length = length
        self.next = {}
        self.link = -1
        self.word = ""



class SuffixAutomaton:
    def __init__(self, s):
        self.longest_length = 0
        self.longest_word = ""
        self.state = []
        self.state.append(State())
        self.last = 0
        for c in s:
            self.add(c)

    def add(self, c):
        if self.last == 0:
            cur = State(1)
            cur.word = c
            cur.link = self.state[0]
            self.state[0].next[c] = cur
            self.state.append(cur)
            self.last = cur
            return
        cur = State(self.last.length + 1)
        cur.word = self.last.word + c

        p = self.last
        while not (c in p.next) and p.link != -1:
            p.next[c] = cur
            p = p.link

        if p.link == -1 and not (c in p.next):
            p.next[c] = cur
            self.last.next[c] = cur
            self.state.append(cur)
            cur.link = p
            self.last = cur
            return

        self.last.next[c] = cur
        self.state.append(cur)
        q = p.next[c]

        if p.length + 1 == q.length:
            cur.link = q
            if q.length > self.longest_length:
                self.longest_length = q.length
                self.longest_word = q.word
            self.last = cur
            return
        clone = State(p.length + 1)
        clone.next = q.next.copy()
        clone.link = q.link
        clone.word = p.word + c
        clone.length = p.length + 1
        cur.link = clone
        q.link = clone

        self.state.append(clone)

        while c in p.next:
            if clone.length < p.next[c].length:
                p.next[c] = clone
            p = p.link
            if p == -1:
                break

        if clone.length > self.longest_length:
            self.longest_length = clone.length
            self.longest_word = clone.word
        self.last = cur

    def getLongest(self):
        return self.longest_word

    def print(self):
        for i in range(len(self.state)):
            print(f'{i}:{self.state[i].word}')

def main():
    s = input()
    suffix_automaton = SuffixAutomaton(s)
    print("longest word: " + suffix_automaton.getLongest())


if __name__ == "__main__":
    main()