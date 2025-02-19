class Item:
    def __init__(self, name, description="", rarity="common"):
        self.name=name
        self.description=""
        self.rarity=rarity
        self._ownership=""

    def pick_up(self,character):
        self._ownership=character
        print(f"{self.name} is now owned by {character}")

    def throw_away(self):
        self._ownership=False
        print(f"{self.name} has been thrown away.")

    def use(self):
        if self._ownership != False and self._ownership != "":
            print(f"{self.name} has been used")

    def __str__(self):
        if self._ownership != False and self._ownership != "":
            owner_string=f"owned by {self._ownership}"
        else:
            owner_string="currently not owned"
        return(f"{self.name} is a {self.rarity} item {owner_string}. Description: {self.description}")

class Weapon(Item):
    def __init__(self, name, damage, type, description="", rarity="common"):
        super().__init__(name, description, rarity)
        self.damage=damage
        self.type=type
        self.equipped=False
        self._attack_modifier=1

    def equip(self):
        if self._ownership != False or self._ownership != "":
            print(f"{self.name} is equipped by {self._ownership}")
            self.equipped=True
        else:
            print("You cannot equip an item that is not owned.")

    def use(self):
        if self.equipped==True and self._ownership!=False and self._ownership != "":
            if self.rarity =="legendary":
                self._attack_modifier=1.15
            attack_power=self.damage*self._attack_modifier
            print(f"{self.name} is used, dealing {attack_power} damage.")

    def __str__(self):
        return(super().__str__() + f"This weapon is a {self.type} with a damage of {self.damage}")

class Shield(Item):
    def __init__(self, name, defense, broken=False, description="", rarity="common"):
        super().__init__(name,description,rarity)
        self.defense=defense
        self.broken=broken
        self.equipped=False
        self.defense_modifier=1
        if self.rarity not in ["common","uncommon","epic"]:
            self._defense_modifier=1.15
        else:
            self._defense_modifier=1

    def equip(self):
        if self._ownership != False or self._ownership != "":
            print(f"{self.name} is equipped by {self._ownership}")
            self.equipped=True
        else:
            print("You cannot equip an item that is not owned.")

    def use(self):
        if self.equipped==True and self._ownership!=False and self._ownership != "":
            if self.broken==False:
                broken_modifier=1
            else:
                broken_modifier=0.5
            defense_level=self.defense*self.defense_modifier*broken_modifier
            print(f"{self.name} is used, blocking {defense_level} damage.")

    def __str__(self):
        return(super().__str__() + f"Defense: {self.defense}, Broken Status: {self.broken}")

class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time, description="", rarity="common"):
        super().__init__(name,description,rarity)
        self.potion_type=potion_type
        self.value=value
        self.effective_time=effective_time
        self.used=False

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        potion = cls(name=name, potion_type=potion_type, value=50, effective_time=30, description='Generated from ability', rarity='common')
        potion._ownership = owner
        return potion

    def use(self):
        if self._ownership!=False and self._ownership!="" and self.used==False:
            self.used=True
            print(f"{self._ownership} used {self.name}, and {self.potion_type} has increased by {self.value} for {self.effective_time} seconds")

    def __str__(self):
        return(super().__str__() + f"Potion Type: {self.potion_type}, Value: {self.value}, Effective Time: {self.effective_time}")



belthronding=Weapon(name="Belthronding",rarity="legendary",damage=5000,type="bow")
belthronding.pick_up("Sally")
belthronding.equip()
belthronding.use()
print(belthronding)

broken_pot_lid=Shield(name="wooden lid",description="A lid made of wood, useful in cooking. No one will choose it willingly fora shield",defense=5,broken=True)
broken_pot_lid.pick_up("Sally")
broken_pot_lid.equip()
broken_pot_lid.use()
broken_pot_lid.throw_away()
broken_pot_lid.use()
print(broken_pot_lid)

attack_potion=Potion.from_ability(name="atk potion temp",owner="Sally",potion_type="attack")
attack_potion.use()
attack_potion.use()
print(attack_potion)

print(isinstance(belthronding,Item))
print(isinstance(broken_pot_lid, Shield))
print(isinstance(attack_potion,Weapon))
