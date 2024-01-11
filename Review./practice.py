import random
def reverse_digits(integer):
    strng = str(integer)
    reverse = " "
    for i in range(len(strng)-1, -1, -1):
        reverse = reverse + strng[i]
    return int(reverse)

def hot_potato(list_names):
    players_in_game = []
    for name in list_names:
        players_in_game.append(name)
    while len(players_in_game) > 1:
        toss = random.randint(1, 5)
        for i in range(toss):
            i = (i + 1) % len(players_in_game)
            print(players_in_game[i-1] + " tosses the potato to " + players_in_game[i])
        print("The music has stopped and the  " + players_in_game[i] + " is holding the potato!")
        players_in_game.pop(i)
    print("Games over!" + players_in_game[0] + " wins the game!")
    
def main():
    print(reverse_digits(2001))
    print(reverse_digits(43))
    print(reverse_digits(123456))
    names_0 = ["Bobby", "Bruce", "Chris", "Dave"] 
    hot_potato(names_0)
    names_1= ["A", "B", "C", "D","E"]
    hot_potato(names_1)
if __name__ == "__main__":
    main()
