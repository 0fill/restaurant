from restaurant import Database

k = input("input your database key: ")  #I used 1
d = Database(k)
while True:
    choice = input(f"""1-add restaurant\n2-remove restaurant\n3-list restaurant\n4-edit restaurant\n5-search for 
    restaurant\n6-exit""")
    if choice == "1":
        d.add(input("input name of the restaurant"), input("input restaurants specialization"),
              input("input restaurants address"),
              input("input restaurants website"), input("phone for restaurant"))
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
