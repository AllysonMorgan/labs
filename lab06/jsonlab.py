import json

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
        legendary_message="""
  _      ______ _____ ______ _   _ _____          _______     __
 | |    |  ____/ ____|  ____| \ | |  __ \   /\   |  __ \ \   / /
 | |    | |__ | |  __| |__  |  \| | |  | | /  \  | |__) \ \_/ /
 | |    |  __|| | |_ |  __| | . ` | |  | |/ /\ \ |  _  / \   /
 | |____| |___| |__| | |____| |\  | |__| / ____ \| | \ \  | |
 |______|______\_____|______|_| \_|_____/_/    \_\_|  \_\ |_|
"""
        if self.rarity=="legendary":
            return(f"{self.name} is a super duper cool LEGENDARY item {owner_string}. Description: {self.description} {legendary_message}")
        else:
            return(f"{self.name} is a {self.rarity} item {owner_string}. Description: {self.description}")
    def to_json(self):
        item_info={
        "Type":self.__class__.__name__,
        "Name":self.name,
        "Description":self.description,
        "Rarity":self.rarity,
        "Ownership":self._ownership
        }
        return item_info
    @classmethod
    def from_json(cls,json_data):
        return cls(
        name=json_data["Name"],
        description=json_data["Description"],
        rarity=json_data["Rarity"])

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

    def to_json(self):
        item_info={
        "Name":self.name,
        "Description":self.description,
        "Rarity":self.rarity,
        "Ownership":self._ownership,
        "Damage":self.damage,
        "Type":self.type,
        "Equipped":self.equipped,
        "Attack Modifier":self._attack_modifier
        }
        return item_info

    @classmethod
    def from_json(cls, json_data):
        name=json_data["Name"]
        description=json_data["Description"]
        rarity=json_data["Rarity"]
        damage=json_data["Damage"]
        type=json_data["Type"]
        equipped=json_data["Equipped"]
        new_instance=cls(name=name, damage=damage, type=type, description=description, rarity=rarity)
        new_instance.equipped=equipped
        return new_instance

class Single_Handed_Weapon(Weapon):
    def _slash(self):
        print("Slash attack!")

class Double_Handed_Weapon(Weapon):
    def _spin(self):
        print("Spin attack!")

class Pike(Weapon):
    def _thrust(self):
        print("Thrust attack!")

class Ranged_Weapon(Weapon):
    def _shoot(self):
        print("Shoot attack!")

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
    def to_json(self):
        item_info={
        "Name":self.name,
        "Description":self.description,
        "Rarity":self.rarity,
        "Ownership":self._ownership,
        "Defense":self.defense,
        "Broken":self.broken,
        "Equipped":self.equipped
        }
        return item_info

    @classmethod
    def from_json(cls,json_data):
        name=json_data["Name"]
        description=json_data["Description"]
        rarity=json_data["Rarity"]
        defense=json_data["Defense"]
        broken=json_data["Broken"]
        equipped=json_data["Equipped"]
        new_instance=cls(name=name, defense=defense, broken=broken, description=description,rarity=rarity)
        new_instance.equipped=equipped
        return new_instance

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

    def to_json(self):
        item_info={
        "Name":self.name,
        "Description":self.description,
        "Rarity":self.rarity,
        "Ownership":self._ownership,
        "Potion Type":self.potion_type,
        "Value":self.value,
        "Effective Time":self.effective_time,
        "Used":self.used
        }
        return item_info

    @classmethod
    def from_json(cls,json_data):
        name=json_data["Name"]
        description=json_data["Description"]
        rarity=json_data["Rarity"]
        potion_type=json_data["Potion Type"]
        value=json_data["Value"]
        effective_time=json_data["Effective Time"]
        used=json_data["Used"]
        new_instance = cls(name=name, potion_type=potion_type, value=value, effective_time=effective_time, description=description, rarity=rarity)
        new_instance.used = used
        return new_instance

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        item._ownership=self.owner
        self.items.append(item)

    def drop_item(self, item):
        if item in self.items:
            item.throw_away()
            self.items.remove(item)

    def view(self, item=None, item_type=None):
        if item_type:
            filtered_items = [item for item in self.items if isinstance(item, item_type)]
            if filtered_items:
                for item in filtered_items:
                    print(item)
            else:
                print(f"No items of type {item_type.__name__} found.")
        else:
            if self.items:
                for item in self.items:
                    print(item)
            else:
                print("Inventory is empty.")
        if item!=None:
            print(item)
    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items
    def to_json(self):
        inventory_info={
        "Ownership":self.owner,
        "Items": [item.to_json() for item in self.items]
        }
        return inventory_info

    @classmethod
    def from_json(cls,json_data):
        inventory=cls(owner=json_data["Ownership"])
        for item_info in json_data["Items"]:
            item_type=item_info.get("Type","Item")
            if item_type=="Weapon":
                item=Weapon.from_json(item_info)
            elif item_type=="Shield":
                item=Shield.from_json(item_info)
            elif item_type=="Potion":
                item=Potion.from_json(item_info)
            else:
                item=Item.from_json(item_info)
            inventory.add_item(item)
        return inventory
class InventoryEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Inventory):
            return obj.to_json()
        return super().default(obj)


#Testing stuff below:


belthronding=Ranged_Weapon(name="Belthronding",rarity="legendary",damage=500,type="bow")
#belthronding.pick_up("Sally")
#belthronding.equip()
#belthronding.use()
#print(belthronding)

broken_pot_lid=Shield(name="wooden lid",description="A lid made of wood, useful in cooking. No one will choose it willingly fora shield",defense=5,broken=True)
#broken_pot_lid.pick_up("Sally")
#broken_pot_lid.equip()
#broken_pot_lid.use()
#broken_pot_lid.throw_away()
#broken_pot_lid.use()
#print(broken_pot_lid)

#attack_potion=Potion.from_ability(name="atk potion temp",owner="Sally",potion_type="attack")
#attack_potion.use()
#attack_potion.use()
#print(attack_potion)

#print(isinstance(belthronding,Item))
#print(isinstance(broken_pot_lid, Shield))
#print(isinstance(attack_potion,Weapon))

hp_potion=Potion(name="Health Potion",potion_type="health",value=10,effective_time=10)
master_sword=Single_Handed_Weapon(name="Master Sword",rarity="legendary",damage=300, type="sword")
muramasa=Double_Handed_Weapon(name="Maramasa",rarity="legendary",damage=580, type="katana")
gungnir=Pike(name="Gungnir",rarity="legendary",damage=290,type="spear")
round_shield=Shield(name="Round Shield",defense=10)

beleg_backpack = Inventory(owner = 'Beleg')
beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(hp_potion)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(round_shield)
#beleg_backpack.view(item_type = Shield)
beleg_backpack.view()
#beleg_backpack.drop_item(broken_pot_lid)
"""
if master_sword in beleg_backpack:
    master_sword.equip()
    print(master_sword)
    master_sword.use()

for item in beleg_backpack:
    if isinstance(item, Weapon):
        beleg_backpack.view(item=item)
"""

#Turning beleg's backpack into json
inventory_json=json.dumps(beleg_backpack,cls=InventoryEncoder,indent=2)
print(inventory_json)

#Example of how the json data needs to be formatted
print("JSON data to create a new inventory must be in the form of dictionaries. Example Format:")
print(json.dumps({
        "Ownership": "ExamplePlayer",
        "Items": [
            {
                "Type": "Weapon",
                "Name": "Sword",
                "Description": "Something something.",
                "Rarity": "common",
                "Ownership": "ExamplePlayer",
                "Damage": 10,
                "Type": "Melee",
                "Equipped": False,
                "Attack Modifier": 1
            },
            {
                "Type": "Shield",
                "Name": "Shield",
                "Description": "A sturdy shield.",
                "Rarity": "common",
                "Ownership": "ExamplePlayer",
                "Defense": 5,
                "Broken": False,
                "Equipped": False
            },
            {
                "Type": "Potion",
                "Name": "Health Potion",
                "Description": "Restores health.",
                "Rarity": "common",
                "Ownership": "ExamplePlayer",
                "Potion Type": "Healing",
                "Value": 20,
                "Effective Time": 30,
                "Used": False
            }
        ]
    }, indent=3))

#Just creating a new inventory using the previously made json data from beleg backpack
new_inventory=Inventory.from_json(json.loads(inventory_json))
new_inventory.view()

#Creating new sword from json format
new_sword={
        "Type": "Weapon",
        "Name": "Cool Sword",
        "Description": "A cool sword!",
        "Rarity": "common",
        "Ownership": "Sally",
        "Damage": 15,
        "Type": "Melee",
        "Equipped": False,
        "Attack Modifier": 1
        }
cool_sword=Weapon.from_json(new_sword)
print(cool_sword)

#Creating a new shield from json format
new_shield={
        "Type": "Shield",
        "Name": "Strong Shield",
        "Description": "A super strong piece of wood",
        "Rarity": "common",
        "Ownership": "Becky",
        "Defense": 10,
        "Broken": False,
        "Equipped": False
        }
strong_shield=Shield.from_json(new_shield)

#Creating a new potion from json format
new_pot={
        "Type":"Potion",
        "Name":"Health Potion",
        "Description":"A weak potion that restores health",
        "Rarity":"Common",
        "Ownership":"Harry Potter",
        "Potion Type":"Healing",
        "Value":15,
        "Effective Time": 15,
        "Used":False
        }
health_potion=Potion.from_json(new_pot)
print(health_potion)
