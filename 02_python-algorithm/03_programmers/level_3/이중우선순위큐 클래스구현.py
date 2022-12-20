from heapq import heappop, heappush

REMOVED = "r"

'''
- min_ele, max_ele = [v, vid], [-v, vid]
- min_ele를 min_heap에, max_ele를 max_heap에 넣고, [min_ele, max_ele]를 entry_finder 딕셔너리에 vid 키에 넣어서 min_heap과 max_heap의 vid의 값이 같은 주소를 가리킨다.
- entry_finder.pop(vid)를 통해 v와 vid가 가리키는 주소를 entries에 할당
- entries[0][1] 혹은 entries[1][1] 인덱싱으로 vid가 가리키는 주소의 값을 REMOVED로 재할당을 통해 min_heap, max_heap에 있는 값도 수정

-> _check_empty 메서드로 vid가 REMOVED로 바뀌었으면 heappop을 통해 갱신해서 진짜 최소값 혹은 최대값을 받는다.
'''


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
        option, num = each.split(" ")
        num = int(num)
        if option == "I":
            dpq.insert(num)
        elif option == "D" and num == -1:
            dpq.pop_min()
        else:
            dpq.pop_max()

    return [dpq.get_max(), dpq.get_min()]

a = solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])

print(a)