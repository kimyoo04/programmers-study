# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
            

# 공격 유닛
class AttackUnit(Unit): # Unit 클래스를 상속 받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
        .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
        .format(self.name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed를 0으로 설정
        Flyable.__init__(self, flying_speed)

    # fly 함수를 move 함수를 재정의 해서 공중 유닛도 move 함수로 실행이 됨.
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(location) # 나도코딩이랑 다름 fly 함수 정의부의 매개변수를 바꿈


# 띄어쓰기
print()

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) # speed는 0
        # 다중 상속 코드에선 super() 를 쓰면 순서상 맨 "처음" 클래스(예제에서는 Flyable) 에 대해서 __init__ 함수가 호출된다.
        # 다중 상속일 댄 supper()쓰지 않기
        super().__init__(name, hp, 0)
        self.location = location