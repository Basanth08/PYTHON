class Avenger:
    __slots__ = ["name","identity","powers","weapons"]
    def __init__(self,name ="",identity="",powers =list(), weapons = list()):
        self.name = name
        self.identity = identity
        self.powers = powers
        self.weapons = weapons

    def print_bio(self):
        print(self.name + " (" + self.identity + "):") 
        print("Powers:")
        for power in self.powers:
                print(power)
        print("Weapons:")
        for weapon in self.weapons:
            print(weapon)

class Team:
    __slots__ = ["member","leader"]
    def __init__(self,member,leader):
        self.member = member
        self.leader = leader
    
    def add_member(self, member):
        self.member.append(member)
    
    def set_leader(self, leader):
        self.leader = leader
        
    def print_roster(self):
        for member in self.member:
            marker = "[Leader] " if member == self.leader else ""
        print(marker + member.name)

    def find_member(self, name):
        for member in self.member:
            if member.name == name:
                return member
        return None
    
    def get_leader(self):
        return self.leader
    
    def print_full_roster(self):
        for member in self.member:
            marker = "[Leader] " if member == self.leader else ""
        print(marker + member.name + ":")
        member.print_bio()

def main():
    ironman = Avenger("Iron Man", "Tony Stark", 
                        ["Genius", "Advanced Armor"], 
                        ["Repulsors", "Missiles"]) 
    captain = Avenger("Captain America", "Steve Rogers",
                    ["Strength", "Agility"],
                    ["Shield"])                 
    # Create more Avengers
    team = Team([ironman,captain],ironman)
    team.add_member(ironman)
    team.add_member(captain)
    # Add more members   
    team.set_leader(ironman) 
    team.print_roster()
    ironman.print_bio()
if __name__ =="__main__":
    main()