# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = False
        self.s_to = False
        self.e_to = False
        self.w_to = False

    def __str__(self):
        return f"{self.name}\n{self.description}"
    
    

    def get_item(self, item):
        self.items.remove(item)

    def list_items(self):
        if len(self.items) < 1:
            print("There is nothing to see here.")
        else:
            print("Upon further inspecting the area you find:")
            for item in self.items:
                print(f" {item}")

    def drop_item(self, item):
        self.items.append(item)