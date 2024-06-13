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
        for ingredient in ingredients:
            if ingredient in self.machine_resources < ingredients:
                #Print insufficient resources
                print(f"Insufficient {ingredients}")
                return False
        #Return true if the above conditional fails
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

### Make an instance of SandwichMachine class and write the rest of the codes ###