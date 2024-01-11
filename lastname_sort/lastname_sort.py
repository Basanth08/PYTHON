"""
    lastname_sort.py
"""

def last_name_sort(name_list):
    new_list = []
    for first_name, last_name in name_list:
        new_list.append((last_name, first_name))
    new_list.sort()
    sorted_list = []
    for last_name, first_name in new_list:
        sorted_list.append((first_name, last_name))
    return sorted_list

def main():
  name_list = [("Graylin","Pugel"),("Jamara","Larive"),("Orry","Eskew"),
                ("Lauro","Gardenas"),("Venise","Tille")]
  result = last_name_sort(name_list)
  print(result)
  name_list2 = [("Vikram","Coldivar"),("Blake","Gommer"),("Taja","Garrick"),
                ("Lynzee","Derrick"),("Leon","Zagar"),("Sherrie","Vermette"),
                ("Jacintha","Mcmanamon"),("Chelse","Tietz"),
                ("Nefertiti","Weidenheimer"),("Devonta","Jurina"),
                ("Chinita","Borgert"),("Christena","Lott"),("Lilia","Szoka"),
                ("Normandy","Curet"),("Anicia","Lemay"),("Odyssey","Naegeli"),
                ("Aleen","Farrel"),("Jazmin","Almaguer"),
                ("Stormie","Kalafarski"),("Christyne","Piascik")]
  result2 = last_name_sort(name_list2)
  print(result2)
if __name__ == "__main__":
    main()