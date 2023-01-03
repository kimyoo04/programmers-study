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
- 날짜가 넘어가는 경우의 비교 방법 -> datetime 모듈 사용
- 슬라이딩 윈도우 활용, 각 로그들의 시작 시간과 끝 시간 주변 탐색, 겹치는 최대의 로그 수 반환
- 작업 시작과 작업 끝 시간의 처리를 어떻게 하는지 파악
- 날짜 비교, 날짜 연산 방법
- float의 경우 셋째 자리까지
'''

# 실패한 사례
def solution1(lines):
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


"""
실패한 이유
- 데이터 가공에 날짜가 빠져서 정확한 작업의 시작시간을 알 수가 없다.
- 마구잡이로 시작해서 자료구조를 어떤 것을 쓸지 확정짓지 않았다.
- 경계값 처리 전략을 정하지 않았다.

다음 시도 전략
- datetime의 strptime, timedelta 메소드를 사용한다.
- 경계값 처리 확실히 한다.
- 슬라이딩 윈도우를 버리고, 모든 작업의 시작, 끝을 탐색돌면서 1초씩 더해 범위 안의 로그를 찾는다.
"""

# 성공한 시도
import datetime

def get_work_time(line):
    # 날짜 / 시간 / 작업시간량
    date, time, work_t = line.split(" ")
    work_t = float(work_t[:-1]) - 0.001

    finish = datetime.datetime.strptime(" ".join([date, time]), "%Y-%m-%d %H:%M:%S.%f")
    start = finish - datetime.timedelta(seconds=work_t)

    return [start, finish]


def solution2(lines):
    max_ = 0
    work_times = []

    for line in lines:
        work_times.append(get_work_time(line))

    for work_time in work_times:
        for time in work_time:
            count_ = 0

            for log in work_times:
                # 범위 끝(+0.999s)이 작업 시작시간보다 작은 경우
                if time + datetime.timedelta(seconds=0.999) < log[0]:
                    continue
                # 범위 시작이 작업 끝시간보다 큰 경우
                elif time > log[1]:
                    continue
                else:
                    count_ += 1

            if count_ > max_:
                max_ = count_

    return max_

a = solution2(
    [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]
)

print(a)

"""
다른 풀이 방법
- 모든 날짜와 시간을 실수타입의 초단위로 바꾼다. (주어진 날짜와 시간을 전부 분할한다.)
    -> 어차피 탐색의 범위는 1초이기 때문에!
- 트레픽이라는 변수명을 사용한다.
- 문자열의 더하기 연산을 적극적으로 활용한다.
- replace를 통한 s 문자를 삭제
"""