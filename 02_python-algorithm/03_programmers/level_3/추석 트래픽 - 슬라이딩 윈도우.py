# https://school.programmers.co.kr/learn/courses/30/lessons/17676

'''
9월 15일 로그 데이터 분석 -> 초당 최대 처리량 계산

초당 최대 처리량 = 요청의 응답 완료 여부에 관계 없이 임의 시간부터 1초간 처리하는 요청의 최대 개수

입력
- ines 배열: N개의 로그 문자열 -> 각 로그 문자열마다 요청에 대한
응답완료시간S 처리시간T  <-- 공백 구분
- 응답완료시간S = 2016-09-15 hh:mm:ss.sss
- 처리시간 T = 0.1s, 0.312s, 2s  <- s로 끝남, 소수점 셋째 자리까지
- 처리시간은 시작시간과 끝시간을 포함
- 서버타임아웃은 3초
- lines는 S를 기준으로 오름차순 정렬 (시간순)

출력
- lines에 대한 초당 최대 처리량 리턴

예제1
01:00:02.003 ~ 01:00:04.002 2.0s
01:00:05.001 ~ 01:00:07.000 2.0s
-> 01:00:04.002에 1을 더하면 01:00:05.002가 되어 01:00:05.001에 시작한 두 번째 로그가 겹쳐서 1초 동안 최대 2개가 된다.
'''

'''
필요한 핵심
- 날짜가 넘어가는 경우의 비교 방법
- 슬라이딩 윈도우 활용, 각 로그들의 시작 시간과 끝 시간 주변 탐색, 겹치는 최대의 로그 수 반환
- 작업 시작과 작업 끝 시간의 처리를 어떻게 하는지 파악
- 날짜 비교, 날짜 연산 방법
- float의 경우 셋째 자리까지
'''

def solution(lines):
    answer = 0
    
    lines = [x.split(" ")[-2:] for x in lines]
    
    new_lines = []
    for line in lines:
        line = [line[0].split(":"), line[1][:-1]]
        new_lines.append(line)        
    
    for a_log in new_lines:
        hh, mm, ss = a_log[0]
        hh, mm = int(hh), int(mm)
        ss = float(ss)
        work_time = float(a_log[1])
        
        print(hh, mm, ss, '-',work_time)
    return answer