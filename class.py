class Pokemon:
    def __init__(self, name: str, max_armor: int, max_hit: int):
        self.name = name
        self.armor = max_armor
        self.hit_points = max_hit

    def attack(self):
        print(f"{self.name} attacks")

    def defend(self):
        print(f"{self.name} defends itself")

    pikachu = Pokemon("Pikachu", 100, 1000)
    pikachu.attack()
    pikachu.attack() 
    pikachu.defend()