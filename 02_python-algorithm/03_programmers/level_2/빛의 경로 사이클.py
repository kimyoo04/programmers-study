def solution(grid):
    V=((1,0),(0,-1),(-1,0),(0,1))           # 방향(예를 들어, [1,0]은 1행 0열 추가하는 방향(아래로))
    def turn(i,j,k):                        # 빛이 격자를 통과한 결과를 보여주는 함수
        if  grid[i][j]=='S' :               # i=행, j=열, k=들어가는 방향
            k=k
            i+=V[k][0]
            j+=V[k][1]
        elif grid[i][j]=='L' : 
            k=(k-1)%4
            i+=V[k][0]
            j+=V[k][1]
        elif grid[i][j]=='R' : 
            k=(k+1)%4
            i+=V[k][0]
            j+=V[k][1]
        i=i%len(grid)
        j=j%len(grid[0])
        return i,j,k

    position_n_direction=[]      # (행,열,방향) 정보를 모아둘 리스트
    answer=[]                    # 경로의 길이 리스트

    # 3중 for 문으로 모든 칸(i, j)과 4가지 방향(k) 탐색
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                n=0
                
                # 이미 계산한 경로 제외 혹은, 반복되는 칸과 방향이 나오면 탈출
                while (i,j,k) not in position_n_direction:
                    position_n_direction.append((i,j,k))
                    i,j,k=turn(i,j,k)
                    n+=1         
                
                if not n==0: answer.append(n) # 경로 길이 기록

    answer.sort()
    return answer