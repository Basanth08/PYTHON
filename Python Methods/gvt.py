COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = ['__name', '__resource_cost', '__rarity', '__faction', '__attack', '__hp']
    
    def __init__(self, name, resource, rarity, faction, attack, hp):
        self.__name = name
        self.__resource_cost = resource
        self.__rarity = rarity
        self.__faction = faction
        self.__attack = attack
        self.__hp = hp
       
    def get_name(self):
        return self.__name
    
    def get_resource_cost(self):
        return self.__resource_cost
    
    def get_rarity(self):
        return self.__rarity
    
    def get_faction(self):
        return self.__faction
    
    def get_attack(self):
        return self.__attack
    
    def get_hp(self):
        return self.__hp
    
    def set_hp(self, new_hp):
        self.__hp = new_hp
        
    def __repr__(self):
        rep_string = (self.__name + '\nRarity: ' + self.__rarity + '\nFaction: ' + self.__faction +
        '\nResource Cost: ' + str(self.__resource_cost) + '\nAttack Power: ' + str(self.__attack) + '\nHP: ' + str(self.__hp))
        return rep_string
    
    def __str__(self):
        rep_string = ('[' + self.__faction[0] + self.__name[0] + ' ' + '{:02d}'.format(self.__resource_cost) +
        ' ' + '{:02d}'.format(self.__attack) + ' ' + '{:02d}'.format(self.__hp) + ']')
        return rep_string
    
    def damage(self, amount):

        if amount <= self.__hp:
            self.__hp -= amount
            return 0
        else:
            current = self.__hp
            self.__hp = 0
            return amount - current
            
    def is_conscious(self):
        if self.__hp > 0:
            return True
        else:
            return False
        
    def __eq__(self, other):

        if type(self) == type(other):
            if self.__attack == other.__attack and self.__faction == other.__faction and self.__rarity == other.__rarity and self.__resource_cost == other.__resource_cost:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):

        if type(self) == type(other):
            if self.__resource_cost == other.__resource_cost:
                return self.__name < other.__name
            else:
                return self.__resource_cost < other.__resource_cost
        return False
     