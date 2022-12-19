from heapq import heappop, heappush

REMOVED = "r"

class DoublePriorityQueue:

    def __init__(self):
        self.entry_finder = {}
        self.min_heap = []
        self.max_heap = []
        self.cnt = 0

    def _check_empty(self, q) -> bool:
        while q and q[0][1] == REMOVED:
            heappop(q)
        if not q:
            return True
        return False

    def insert(self, v):
        vid = self.cnt
        min_ele, max_ele = [v, vid], [-v, vid]
        heappush(self.min_heap, min_ele)
        heappush(self.max_heap, max_ele)
        self.entry_finder[vid] = [min_ele, max_ele]
        self.cnt += 1

    def pop_min(self):
        is_empty = self._check_empty(self.min_heap)
        if not is_empty:
            value, vid = heappop(self.min_heap)
            entries = self.entry_finder.pop(vid)
            entries[1][1] = REMOVED

    def pop_max(self):
        is_empty = self._check_empty(self.max_heap)
        if not is_empty:
            value, vid = heappop(self.max_heap)
            entries = self.entry_finder.pop(vid)
            entries[0][1] = REMOVED

    def get_min(self):
        if not self._check_empty(self.min_heap):
            return self.min_heap[0][0]
        return 0

    def get_max(self):
        if not self._check_empty(self.max_heap):
            return - self.max_heap[0][0]
        return 0


def solution(operations):
    dpq = DoublePriorityQueue()

    for each in operations:
        op, num = each.split(" ")
        num = int(num)
        if op == "I":
            dpq.insert(num)
        elif op == "D" and num == -1:
            dpq.pop_min()
        else:
            dpq.pop_max()

    return [dpq.get_max(), dpq.get_min()]

a = solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])

print(a)