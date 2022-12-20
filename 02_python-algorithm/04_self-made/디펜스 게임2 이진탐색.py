def solution (n, m, k, enemy):
    start, end = 0, len(enemy)
    mid = (start + end) // 2
    
    while start <= end:
        rounds = sorted(enemy[:mid], reverse=True)
        skill = k

        remain = 0
        for round_enemy in rounds:
            if skill > 0:
                skill -= 1
            else:
                remain += round_enemy
        
        print(rounds, skill, remain, start, mid, end)

        if  (m * 2) + n - remain >= 0 and skill >= 0: 
            start = mid + 1
            print("start", start)
        else: 
            end = mid - 1
            print("end", end)
        mid = (start + end) // 2
        
    return start - 1

a = solution(7, 3, 3, [4, 2, 4, 5, 3, 3, 1, 4, 3])
print(a)