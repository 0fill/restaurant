import pickle
import json


class Restaurant:
    def __init__(self, restaurant_name, specialization, address, website, ph_number):
        self.restaurant_name = restaurant_name
        self.specialization = specialization
        self.address = address
        self.website = website
        self.ph_number = ph_number
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
    def __init__(self, id):
        self.__id = id
        self.path = f"data/{id}_restaurants.pkl"
        f = open(self.path, "wb")
        pickle.dump([], f)
        f.close()


    def load(self):
        return pickle.load(open(self.path), "rb")

    def add(self, restaurant_name, specialization, address, website, ph_number):
        data = Database.load()
        pickle.dump(Restaurant(restaurant_name, specialization, address, website, ph_number),open(self.path, "wb"))



    def display(self):
        data = pickle.load(open(self.path, "rb"))
        for r in data:
            print(f"""{r.restaurant_name}: best in {r.specialization} you can find them at {r.address} or at {r.website}
and they deliver to home just call {r.ph_number}""")

    @staticmethod
    def search(id,restaurant_name):
        data = pickle.load(open(f"data/{id}_restaurants.pkl", "rb"))
        for r in data.restaurant_name:
            if restaurant_name in r:
                if input(f"is the restaurant you're looking for {restaurant_name}?").lower() == "y":
                    return r
        return None

    def remove(self):
        restaurant_name = Restaurant.search(self.__id,input("which restaurant you want to remove: "))
        data = pickle.load(open(self.path, "rb"))
        data.remove(restaurant_name)








r = Restaurant("antonio", "italiano", "adda7", "aaa.www", "7854785")

#print(Restaurant.from_pickle())
