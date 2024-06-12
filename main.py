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


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        #Process bills, nickels, quarters, half dollars
        while True:
            try:
                dollar = int(input("How many dollars?: "))
                half_dollar = int(input("How many half dollars? "))
                quarters = int(input("How many quarters? "))
                nickels = int(input("How many nickles? "))
                if dollar < 0 or half_dollar < 0  or quarters < 0 or nickels < 0:
                    raise ValueError("Negative values are not allowed")
                break
            except ValueError as error:
                print(f"Invalid input, {error}, please try again.")

        #Money logic: quarters times .25, nickels times .05, half dollars times .5
        #Total the money
        total = dollar + (half_dollar * .5) + (quarters * .25) + (nickels * .05)
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""


### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = SandwichMachine(resources)
coin = sandwich_machine.process_coins()
print(f"{coin}")