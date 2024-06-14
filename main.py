# Ethan Piland

### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #Need to compare sandwich ingredients with resources
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        while True:
            try:
                dollar = int(input("How many dollars?: "))
                half_dollar = int(input("How many half dollars?: "))
                quarter = int(input("How many quarters?: "))
                nickel = int(input("How many nickels?: "))
                if (dollar < 0 or half_dollar < 0 or quarter < 0 or nickel < 0):
                    raise ValueError("Negatives not allowed")
                break
            except ValueError as e:
                print(f"Invalid input, {e}, please try again.")

        total = dollar + (half_dollar * .5) + (quarter * 0.25) + (nickel * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if (coins < cost):
            #Print insufficient fund
            print("Insufficient funds.")
            return False
        #Print change in this method
        print(f"Change: {coins - cost}")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        ###Check sandwich size, take the resources required from resources
        if sandwich_size in recipes:
            for ingredient, amount in order_ingredients.items():
                self.machine_resources[ingredient] -= amount

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwich_machine = SandwichMachine(resources)
while True:
    try:
        #5 options
        choice = input("What would you like? (small/medium/large/off/report): ").lower()
        #Check if off first, and break the while loop
        if choice == "off":
            print("Turning off the machine.")
            break
        #Check if choice is a report, and print current resources
        elif choice == "report":
            print(f"Bread: {sandwich_machine.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_machine.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_machine.machine_resources['cheese']} ounce(s)")
        #Check if choice is a valid choice, "small", "medium", "large"
        elif choice in recipes:
            order_ingredients = recipes[choice]["ingredients"]
            order_cost = recipes[choice]["cost"]

            #error
            if sandwich_machine.check_resources(order_ingredients):
                print("Please insert coins.")
                total_coins = sandwich_machine.process_coins()

                if sandwich_machine.transaction_result(total_coins, order_cost):
                    sandwich_machine.make_sandwich(choice, order_ingredients)
                    print(f"{choice.capitalize()} sandwich is ready. Bon appetit!")
        else:
            raise ValueError("Invalid input")
    except ValueError as e:
        print(f"{e}, please try again.")