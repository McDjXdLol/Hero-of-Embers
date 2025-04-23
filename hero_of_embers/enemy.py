from hero_of_embers.entity import Entity

class Enemy(Entity):
    def __init__(self, name="Wolf", hp=100, armor=100, damage=15, experience=20, money=20):
        super().__init__(name, hp, armor, damage)
        self.experience_drop = experience
        self.money_drop = money
