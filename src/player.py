# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, inventory = []):
        self.name = name
        self.location = location
        self.inventory = inventory

    def move(self, direction):
        invalid = "There is nothing in that direction, please go another way."
        if direction == 'n':
            if self.location.n_to:
               self.location = self.location.n_to
            else:
                print(invalid)
        elif direction == 's':
            if self.location.s_to:
               self.location = self.location.s_to
            else:
                print(invalid)
        elif direction == 'e':
            if self.location.e_to:
               self.location = self.location.e_to
            else:
                print(invalid)
        elif direction == 'w':
            if self.location.w_to:
               self.location = self.location.w_to
            else:
                print(invalid)

    def get_item(self, item):
        selection = None
        for i in self.location.items:
            if i.name.lower() == item:
                selection = i
            else:
                continue
        if selection != None:
            self.inventory.append(selection)
            self.location.get_item(selection)
            selection.on_take()
        else:
            print(f"You look around but there is no {item} in sight")

    def list_inventory(self):
        if len(self.inventory) < 1:
            print("You are not currently carrying anything")
        else:
            print("Your Inventory:")
            for item in self.inventory:
                print(f" {item}")

    def drop_item(self, item):
        selection = None
        for i in self.inventory:
            if i.name.lower() == item:
                selection = i
            else:
                continue
        if selection != None:
            self.inventory.remove(selection)
            self.location.drop_item(selection)
            selection.on_drop()
        else:
            print(f"You do not currently have {item} in your inventory.")