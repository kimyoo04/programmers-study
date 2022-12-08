# 전달값과 반환값
def deposit(balance, money): # 입금 
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money
# return 반환값.
balance = 0 
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money): # 출금
    if balance >= money: 
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else: 
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return(balance)

def withdraw_night(balance, money): 
    commission = 100
    return commission, balance - money - commission  # 튜플형식으로 반환 가능 


balance = 0 
balance = deposit(balance, 1000)  # 입금 1000원 
# balance = withdraw(balance, 2000) # 출금 2000원 못해. 잔액 1000원 밖에 없어서 
# balance = withdraw(balance, 500)  # 출금 할 수 있다. 잔액 500원 
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))