import pickle
import os


class Restaurant:
    def __init__(self, restaurant_name, specialization, address, website, ph_number):
        self.restaurant_name = restaurant_name
        self.specialization = specialization
        self.address = address
        self.website = website
        self.ph_number = ph_number

    def display_restaurant_info(self):
        print(self.restaurant_name, self.specialization, self.address, self.website, self.ph_number)

    def __eq__(self, other):
        return self.address == other.address or self.ph_number == other.ph_number or self.website == other.website

    @staticmethod
    def my_in (item: 'Restaurant', list):
        for i in list:
            if i == item:
                return True
        return False


class Database:
    def __init__(self, id):
        self.__id = id
        self.path = f"data/{id}_restaurants.pkl"
        if os.path.exists(self.path):
            return
        with open(self.path, "wb") as f:
            pickle.dump([], f)

    def load(self):
        return pickle.load(open(self.path, "rb"))

    def add(self, restaurant_name, specialization, address, website, ph_number):
        data = self.load()
        new_r = Restaurant(restaurant_name, specialization, address, website, ph_number)
        if not Restaurant.my_in(new_r, data):
            data.append(new_r)
            pickle.dump(data, open(self.path, "wb"))
        else:
            print("Restaurant already exists")

    def display(self):  #5
        data = self.load()
        for r in data:
            print(f"""{r.restaurant_name}: best in {r.specialization} you can find them at {r.address} or at {r.website}
and they deliver to home just call {r.ph_number}""")

    @staticmethod
    def search(my_id, restaurant_name):
        data = pickle.load(open(f"data/{my_id}_restaurants.pkl", "rb"))
        for r in data:
            if restaurant_name.lower() in r.restaurant_name.lower():
                if input(f"is the restaurant you're looking for {r.restaurant_name}?").lower() == "y":
                    return r.restaurant_name
        return None

    def remove(self):  #6
        restaurant_name = Database.search(self.__id, input("which restaurant you want to remove: "))
        data = self.load()
        for r in data:
            if r.restaurant_name == restaurant_name:
                data.remove(r)
        pickle.dump(data, open(self.path, "wb"))

    def edit(self):
        r_name = Database.search(self.__id, input("which restaurant you want to edit: "))
        if r_name is None:
            return
        data = self.load()
        choice = input(f"what would you like to edit? \n n for name\n s for specialization\n a for address\n w for "
                       f"website\n p for phone number\n:")
        for r in data:
            if r.restaurant_name == r_name:
                if choice == "n":
                    r.restaurant_name = input("new restaurant name: ")
                elif choice == "s":
                    r.specialization = input("new restaurant specialization: ")
                elif choice == "a":
                    r.address = input("new restaurant address: ")
                elif choice == "w":
                    r.website = input("new restaurant website: ")
                elif choice == "p":
                    r.ph_number = input("new restaurant phone number: ")
                else:
                    return None

    def adv_search(self):
        data = self.load()
        choice = input(f"what would you like to search by?\n n for name\n s for specialization\n a for address\n w for "
                       f"website\n p for phone number\n: ")
        if choice == "n":
            m = lambda x: x.restaurant_name
            s = input("which restaurant you want to search: ")
        elif choice == 's':
            m = lambda x: x.specialization
            s = input("which specialization you want to search: ")
        elif choice == "a":
            m = lambda x: x.address
            s = input("which address you want to search: ")
        elif choice == "w":
            m = lambda x: x.website
            s = input("which website you want to search: ")
        elif choice == "p":
            m = lambda x: x.ph_number
            s = input("which phone number you want to search: ")
        else:
            return
        for r in data:
            if s.lower() in m(r).lower():
                r.display_restaurant_info()
