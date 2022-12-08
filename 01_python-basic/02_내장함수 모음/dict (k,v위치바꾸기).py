# key value 위치 바꾸기 (딕셔너리 컴프리핸션)
dialDic = {1:"abc", 2:"cde", 3:"fgh"}
print(dialDic)

dialDic2 = {}
dialDic2 = {v:k for k,v in dialDic.items()}
print(dialDic2)

# 예제용 딕셔너리 만들기
di = dict(zip('abcde',range(5)))
print(di)

# key value 위치 바꾸기 (zip, dict 사용)
di = dict(zip(di.values(),di.keys()))




