import pets

def main():
    pet1 = pets.Pet("Dog", "Fido", 10, "White", 7)
    print("Name:", pet1.get_name())
    print("Weight:", pet1.get_weight())
    print("Species:", pet1.get_species) 
    print("Fur Color:", pet1.get_fur_color) 
    print("Age:", pet1.get_age)

if __name__ =="__main__":
    main()