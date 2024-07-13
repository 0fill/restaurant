from restaurant import Restaurant,Database

"""database = Database(1)
database.add("U Tří růží", "Česká kuchyně", "Pražská 123, 110 00 Praha", "www.utriruzi.cz", "+420 123 456 789")
database.add("La Trattoria", "Italská kuchyně", "Náměstí Republiky 456, 120 00 Praha", "www.latrattoria.cz", "+420 987 654 321")
database.add("Sushi Bar", "Japonská kuchyně", "Vodičkova 789, 120 00 Praha", "www.sushibar.cz", "+420 555 123 456")
database.add("Le Bistro", "Francouzská kuchyně", "Pařížská 101, 110 00 Praha", "www.lebistro.cz", "+420 777 888 999")
database.add("Tandoori Palace", "Indická kuchyně", "Štěpánská 246, 110 00 Praha", "www.tandooripalace.cz", "+420 111 222 333")
database.add("Pizza Express", "Italská kuchyně", "Václavské náměstí 789, 110 00 Praha", "www.pizzaexpress.cz", "+420 444 555 666")
database.add("Sushi Garden", "Japonská kuchyně", "Na Příkopě 123, 110 00 Praha", "www.sushigarden.cz", "+420 777 888 000")
database.add("El Greco", "Řecká kuchyně", "Ovocný trh 456, 110 00 Praha", "www.elgreco.cz", "+420 124 456 789")
database.add("Thai Spice", "Thajská kuchyně", "Národní třída 789, 110 00 Praha", "www.thaispice.cz", "+420 988 654 321")
database.add("Burger Heaven", "Americká kuchyně", "Dlouhá 101, 110 00 Praha", "www.burgerheaven.cz", "+420 121 222 333")
database.edit()
"""

k = input("input your database key: ")
d = Database(k)
while True:
    choice = input(f"""1-add restaurant\n2-remove restaurant\n3-list restaurant\n4-edit restaurant\n5-search for restaurant\n5-exit""")
    if choice == "1":
        d.add(input("input name of the restaurant"), input("input restaurants specialization"), input("input restaurants specialization"), input("input restaurants address"), input("input restaurants website"), input("input restaurants delivery phone"))
    elif choice == "2":
        d.remove()
    elif choice == "3":
        d.display()
    elif choice == "4":
        d.edit()
    elif choice == "5":
        d.adv_search()
    elif choice == "6":
        break

