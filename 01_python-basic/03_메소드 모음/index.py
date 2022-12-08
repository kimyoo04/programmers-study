# 2-2) index( )

# 찾는 문자가 없는 경우에 ValueError 에러가 발생한다.

# 문자열, 리스트, 튜플 자료형에서 사용 가능하고 딕셔너리 자료형에는 사용할 수 없어 AttributeError 에러가 발생한다.

a = 'oxoxoxoxox'.index('x', 2)

print(a)