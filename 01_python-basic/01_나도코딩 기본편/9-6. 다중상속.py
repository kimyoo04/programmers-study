# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # Unit 클래스를 상속 받음
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# __init__(self, name, hp, damage, flying_speed)
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly("3시") # 김유가 수정함 fly 함수 부분 name 파라미터를 self.name으로 바꿈
valkyrie.attack("3시")
valkyrie.damaged(100) # 발키리의 hp는 200
valkyrie.damaged(100)