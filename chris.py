# This is where Chris will provide his parts of the project.

class Inventory:
    """
    Class containing an inventory and its maximum capacity.
    """
    def __init__(self, items, max):
        self.items = items
        self.max = max
    
    def add(self, item):
        """
        Takes 1 item and adds it to the inventory, given it has enough space.
        """
        if len(self.items) < self.max:
            self.items.append(item)
            return f"{item.name} has been added to your inventory."
        else:
            return "There is not enough space in your inventory!"

    def remove(self, item: str):
        try:
            self.items.pop(self.items.index(item))
            return f"{item.name} has been dropped."
        except ValueError:
            pass
