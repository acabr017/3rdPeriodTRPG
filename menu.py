# class Menu:

#     def __init__(self,options:list):
#         self.options = options

#     def display(self):
# import keyboard

# options = ["A", "B", "C"]
# cursor = 0
# while True:
#     for i, item in enumerate(options):
#         if i == cursor:
#             print(f"> {item}")
#         else:
#             print(item)
#     if keyboard.is_pressed("up"):
#         if cursor == 0:
#             cursor = len(options) - 1
#         else:
#             cursor -= 1
#     elif keyboard.is_pressed("down"):
#         if cursor == len(options) - 1:
#             cursor = 0
#         else:
#             cursor += 1

import cutie


def main():
    options = ["View Inventory", "Drop Items", "Exit"]
    print("What would you like to do?")
    output = options[cutie.select(options)]
    print(output)


if __name__ == "__main__":
    main()
