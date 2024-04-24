print("Welcome to Codetown Burger Co!")


number_of_burgers = 0
# Validate input for number of burgers to be between 1 and 10, also catching ValueError
while number_of_burgers < 1 or number_of_burgers > 10:
    while True:
        try:
            number_of_burgers = int(
                input("How many burgers would you like to order [1-10]? ")
            )
            break
        except ValueError:
            print("Number of burgers must be a number between 1 and 10 (inclusively).")

# declare the burger ingredient variables
bun_type_list = ["milk", "gluten free"]
bun_type = ""

sauce_list = ["tomato", "barbecue", "none"]
sauce = ""

number_of_patties_list = [0, 1, 2, 3]
number_of_patties = -1

number_of_cheese_slices_list = [0, 1, 2, 3]
number_of_cheese_slices = -1

tomato_choice = ""
tomato_choice_list = ["yes", "no"]
has_tomato = False

lettuce_choice = ""
lettuce_choice_list = ["yes", "no"]
has_lettuce = False

onion_choice = ""
onion_choice_list = ["yes", "no"]
has_onion = False


overall_total_cost = 0

# loop through each burger based on how many burgers user entered
for i in range(number_of_burgers):
    # base cost of burger is $5
    total_cost = 5
    print(f"Details for Burger {i+1}:")

    # Check each ingredient input and increase the total cost accordingly if there is extra ingredients from the base burger
    bun_type = input(
        f"\tWhat bun type should be included for Burger {i+1} {bun_type_list}? "
    ).lower()
    while bun_type not in bun_type_list:
        bun_type = input(
            f"Please enter a valid choice: {bun_type_list}\n\tWhat bun type should be included for Burger {i+1} {bun_type_list}? "
        ).lower()
    if bun_type == "gluten free":
        total_cost += 1

    sauce = input(
        f"\tWhat sauce should be included on Burger {i+1} {sauce_list}? "
    ).lower()
    while sauce not in sauce_list:
        sauce = input(
            f"Please enter a valid choice: {sauce_list}\n\tWhat sauce should be included on Burger {i+1} {sauce_list}? "
        ).lower()
    while True:
        try:
            number_of_patties = int(
                input(f"\tHow many patties should be on Burger {i+1} [0-3]? ")
            )
            break
        except ValueError:
            print(f"Please enter a valid choice: {number_of_patties_list}")
    while number_of_patties not in number_of_patties_list:
        while True:
            try:
                number_of_patties = int(
                    input(
                        f"Please enter a valid choice: {number_of_patties_list}\n\tHow many patties should be on Burger {i+1} [0-3]? "
                    )
                )
                break
            except ValueError:
                continue
    if number_of_patties > 1:
        number_of_extra_patties = number_of_patties - 1
        total_cost = total_cost + (number_of_extra_patties * 3)

    while True:
        try:
            number_of_cheese_slices = int(
                input(f"\tHow many slices of cheese should be on Burger {i+1} [0-3]? ")
            )
            break
        except ValueError:
            print(f"Please enter a valid choice: {number_of_cheese_slices_list}")
    while number_of_cheese_slices not in number_of_cheese_slices_list:
        while True:
            try:
                number_of_cheese_slices = int(
                    input(
                        f"Please enter a valid choice: {number_of_cheese_slices_list}\n\tHow many slices of cheese should be on Burger {i+1} [0-3]? "
                    )
                )
                break
            except ValueError:
                continue
    if number_of_cheese_slices > 1:
        number_of_extra_cheese_slices = number_of_cheese_slices - 1
        total_cost = total_cost + (number_of_extra_cheese_slices * 1)

    has_tomato, has_lettuce, has_onion = False
    tomato_choice = input(
        f"\tShould Burger {i+1} have tomato {tomato_choice_list}? "
    ).lower()
    while tomato_choice not in tomato_choice_list:
        tomato_choice = input(
            f"Please enter a valid choice: {tomato_choice_list}\n\tShould Burger {i+1} have tomato {tomato_choice_list}? "
        ).lower()
    if tomato_choice == "yes":
        has_tomato = True

    lettuce_choice = input(
        f"\tShould Burger {i+1} have lettuce {lettuce_choice_list}? "
    ).lower()
    while lettuce_choice not in lettuce_choice_list:
        lettuce_choice = input(
            f"Please enter a valid choice: {lettuce_choice_list}\n\tShould Burger {i+1} have lettuce {lettuce_choice_list}? "
        ).lower()
    if lettuce_choice == "yes":
        has_lettuce = True

    onion_choice = input(
        f"\tShould Burger {i+1} have onion {onion_choice_list}? "
    ).lower()
    while onion_choice not in onion_choice_list:
        onion_choice = input(
            f"Please enter a valid choice: {onion_choice_list}\n\tShould Burger {i+1} have onion {onion_choice_list}? "
        ).lower()
    if onion_choice == "yes":
        has_onion = True

    salad_choices = [has_tomato, has_lettuce, has_onion]

    if all(salad_choices):
        total_cost += 2
    elif salad_choices.count(True) == 2:
        total_cost += 1

    # overall total cost increase with total cost of each burger after each iteration
    overall_total_cost += total_cost

print(f"Total cost for the {number_of_burgers} burger(s): ${overall_total_cost}")
