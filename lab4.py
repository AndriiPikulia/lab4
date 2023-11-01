class Smartphone:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def year_difference(self):
        return 2023 - self.year

class Shop:
    def __init__(self):
        self.smartphones = []

    def add(self, smartphone):
        self.smartphones.append(smartphone)
        print("Added smartphone:", smartphone.name)

    def delete(self, name):
        for smartphone in self.smartphones:
            if smartphone.name == name:
                self.smartphones.remove(smartphone)
                print("Smartphone deleted:", name)
                break
        else:
            print(f"Smartphone '{name}' not found")

    def smartphone_list(self, year):
        sorted_smartphones = [s for s in self.smartphones if s.year >= year]
        if sorted_smartphones:
            print("Smartphones released after:", year)
            for smartphone in sorted_smartphones:
                year_difference = smartphone.year_difference()
                print(f"{smartphone.name} ({smartphone.year}), {year_difference} years after release")
        else:
            print(f"Smartphones released after {year} not found")

shop = Shop()

while True:
    print("What do you need to do?")
    print("1. Add smartphone")
    print("2. Delete smartphone")
    print("3. Display the list of smartphones")
    print("4. Exit")
    n = int(input("\nSelect option: "))

    if n == 1:
        name = input("Enter smartphone name: ")
        year = int(input("Enter release year of smartphone: "))
        if year > 2023:
            print("Enter a year no greater than 2023")
            break
        phone = Smartphone(name, year)
        shop.add(phone)
        print("\n")

    elif n == 2:
        name = input("Enter smartphone name which you want to delete: ")
        shop.delete(name)
        print("\n")

    elif n == 3:
        input_year = int(input("Enter year: "))
        if input_year > 2023:
            print("Enter a year no greater than 2023")
            break
        shop.smartphone_list(input_year)
        print("\n")

    elif n == 4:
        exit()