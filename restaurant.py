import pickle, os
import json


class Restaurant:
    def __init__(self, restaurant_name, specialization, address, website, ph_number):
        self.restaurant_name = restaurant_name
        self.specialization = specialization
        self.address = address
        self.website = website
        self.ph_number = ph_number

    def display_restaurant_info(self):
        print(self.restaurant_name, self.specialization, self.address, self.website, self.ph_number)
        """try:
            data = pickle.load(open('data/restaurant.pkl', 'rb'))
        except EOFError:
            data = []
        print(data)
        #with open("data/restaurant.pkl", "wb") as file:
           # pickle.dump(data.append(self), file)


    def to_pickle(self):
        with open("data/restaurant.pkl", "wb") as file:
            pickle.dump(pickle.load(open("data/restaurant.pkl", "rb")).append(self), file)

    @staticmethod
    def from_pickle():
        with open("data/restaurant.pkl", "rb") as file:
            return pickle.load(file)
"""


class Database:
    def __init__(self, id: str):
        while os.path.exists(f"data/{id}_restaurants.pkl"):
            id = input("this id is already taken, please chose diffrent: ")
        self.__id = id
        self.path = f"data/{id}_restaurants.pkl"
        with open(self.path, "wb") as f:
            pickle.dump([], f)

    def load(self):
        return pickle.load(open(self.path), "rb")

    def add(self, restaurant_name, specialization, address, website, ph_number):
        data = self.load()
        data.append(Restaurant(restaurant_name, specialization, address, website, ph_number))
        pickle.dump(data, open(self.path, "wb"))

    def display(self):  #5
        data = self.load()
        for r in data:
            print(f"""{r.restaurant_name}: best in {r.specialization} you can find them at {r.address} or at {r.website}
and they deliver to home just call {r.ph_number}""")

    @staticmethod
    def search(my_id, restaurant_name):
        data = pickle.load(open(f"data/{my_id}_restaurants.pkl", "rb"))
        for r in data.restaurant_name:
            if restaurant_name in r:
                if input(f"is the restaurant you're looking for {restaurant_name}?").lower() == "y":
                    return r
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
        choice = input(f"what would you like to edit?  n for name\n s for specialization\n a for address\n w for "
                       f"website\n p for phone number")
        for r in data:
            if r.restaurant_name == r_name:
                if choice == "n":
                    r.restaurant_name = input("new restaurant name")
                elif choice == "s":
                    r.specialization = input("new restaurant specialization")
                elif choice == "a":
                    r.address = input("new restaurant address")
                elif choice == "w":
                    r.website = input("new restaurant website")
                elif choice == "p":
                    r.ph_number = input("new restaurant phone number")
                else:
                    return None

    def adv_search(self):
        data = self.load()
        choice = input(f"what would you like to search by?  n for name\n s for specialization\n a for address\n w for "
                       f"website\n p for phone number")
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
            if s in m(r):
                print(r.display_restaurant_info())
