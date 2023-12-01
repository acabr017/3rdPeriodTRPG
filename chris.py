# This is where Chris will provide his parts of the project.

class Inventory:
    """
    Class containing an inventory and its maximum capacity.
    """
    def __init__(self, items=[], max=20):
        self.items = items
        self.max = max
    
    def add(self, item) -> str:
        """
        Takes 1 item and adds it to the inventory, given it has enough space.
        """
        if len(self.items) < self.max:
            self.items.append(item)
            return f"{item.name} has been added to your inventory."
        else:
            return "There is not enough space in your inventory!"

    def find(self, item: str) -> int:
        """
        Finds specified item and returns its index in the inventory. Returns -1 if no such item.
        """
        for i in range(len(self.items)):
            if self.items[i].name == item:
                return i
        return -1
    
    def remove(self, item: str) -> str:
        """
        Removes specified item from inventory given its name.
        """
        item_index = self.items.find(item)
        if item_index >= 0:
            dropped_item = self.items[item_index].name
            self.items.pop(item_index)
            return f"{dropped_item} has been dropped"
        else:
            return "" # IDK what to return here
