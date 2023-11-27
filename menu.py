# Sample Menu
# Check docs for more info: https://pypi.org/project/cutie/

import cutie


def main():
    options = ["View Inventory", "Drop Items", "Exit"]
    print("What would you like to do?")
    output = options[cutie.select(options)]
    print(output)


if __name__ == "__main__":
    main()
