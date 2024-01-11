import lastname_sort 

def test_empty():
    # setup
    unsorted = []
    expected = []

    # invoke
    actual = lastname_sort.last_name_sort(unsorted)

    assert actual == expected

def test_1():
    # setup
    unsorted = [("Darrell","Matley")]
    expected = [("Darrell","Matley"),]

    # invoke
    actual = lastname_sort.last_name_sort(unsorted)

    assert actual == expected

def test_short():
    # setup
    unsorted = [("Graylin","Pugel"),("Jamara","Larive"),("Orry","Eskew"),
                ("Lauro","Gardenas"),("Venise","Tille")]
                
    expected = [("Orry","Eskew"),("Lauro","Gardenas"),("Jamara","Larive"),
                ("Graylin","Pugel"),("Venise","Tille")]

    # invoke
    actual = lastname_sort.last_name_sort(unsorted)

    assert actual == expected

def test_long():
    # setup
    unsorted = [("Vikram","Coldivar"),("Blake","Gommer"),("Taja","Garrick"),
                ("Lynzee","Derrick"),("Leon","Zagar"),("Sherrie","Vermette"),
                ("Jacintha","Mcmanamon"),("Chelse","Tietz"),
                ("Nefertiti","Weidenheimer"),("Devonta","Jurina"),
                ("Chinita","Borgert"),("Christena","Lott"),("Lilia","Szoka"),
                ("Normandy","Curet"),("Anicia","Lemay"),("Odyssey","Naegeli"),
                ("Aleen","Farrel"),("Jazmin","Almaguer"),
                ("Stormie","Kalafarski"),("Christyne","Piascik")]
        
    expected = [("Jazmin","Almaguer"),("Chinita","Borgert"),
                ("Vikram","Coldivar"),("Normandy","Curet"),("Lynzee","Derrick"),
                ("Aleen","Farrel"),("Taja","Garrick"),("Blake","Gommer"),
                ("Devonta","Jurina"),("Stormie","Kalafarski"),
                ("Anicia","Lemay"),("Christena","Lott"),
                ("Jacintha","Mcmanamon"),("Odyssey","Naegeli"),
                ("Christyne","Piascik"),("Lilia","Szoka"),("Chelse","Tietz"),
                ("Sherrie","Vermette"),("Nefertiti","Weidenheimer"),
                ("Leon","Zagar")]

    # invoke
    actual = lastname_sort.last_name_sort(unsorted)

    assert actual == expected