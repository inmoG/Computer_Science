class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        self.speed = speed

    def move(self, location):
        print("?????? ?????? ??????")
        print(f"{self.name}, {location}, {self.speed}")

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print(f"{self.name} : {location} ???????????? ????????? ?????? ?????????. ????????? {self.damage}")

    def damaged(self, damage):
        print(f"{self.name} : {damage} ???????????? ???????????????. ")
        self.hp -= damage
        print(f"{self.name} : ?????? ????????? {self.hp}?????????.")
        if self.hp <= 0:
            print(f"{self.name} ?????????????????????.")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name}, {location} ???????????? ???????????????. : {self.flying_speed}")


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # ?????? ????????? 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("?????? ?????? ??????")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # ?????? ?????? ????????? super()??? ???????????? ?????? ???????????? ????????????.
        self.location = location