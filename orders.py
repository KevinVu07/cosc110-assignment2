# import burger

burger_order_dict = {}


def main():
    try:
        with open("orders.txt") as file:
            for line in file:
                burger_order = convert_to_tuple(line)
                if burger_order not in burger_order_dict:
                    burger_order_dict[burger_order] = 1
                else:
                    burger_order_dict[burger_order] += 1
    except FileNotFoundError:
        print(
            "Error in reading file. Please double check the filepath or if the file existed."
        )
        SystemExit

    sorted_burger_order_list = sorted(
        sorted(burger_order_dict.items()), key=lambda x: x[1], reverse=True
    )
    print(sorted_burger_order_list)

    orders_to_display = 0
    while orders_to_display <= 0:
        while True:
            try:
                orders_to_display = int(
                    input(
                        "How many of the top burger orders would you like to output? "
                    )
                )
                break
            except ValueError:
                print("Invalid value. Please enter a positive integer")
        if orders_to_display > 0:
            break
        print("Invalid value. Please enter a positive integer")

    print("The top burger orders were:")
    displayTopOrders(orders_to_display, sorted_burger_order_list)


def displayTopOrders(orders_to_display, order_list):
    orders_to_display = (
        len(order_list) if orders_to_display >= len(order_list) else orders_to_display
    )
    for i in range(orders_to_display):
        burger_order = order_list[i][0]
        burger_cost = get_cost(burger_order)
        number_of_order = burger_order_dict[burger_order]
        print(f"{burger_order}\t{number_of_order}\t${burger_cost}")


def convert_to_tuple(line):
    """reading data from orders.txt, return a tuple with entries:
    bun: milk / gluten free
    sauce: tomato / barbecue / none
    number_of_patties: integer
    number_of_cheese_slices: integer
    has_tomato: True / False
    has_lettuce: True / False
    has_onion: True / False
    """
    (
        bun,
        sauce,
        number_of_patties,
        number_of_cheese_slices,
        has_tomato,
        has_lettuce,
        has_onion,
    ) = (
        line.strip().lower().split(",")
    )

    try:
        number_of_patties = int(number_of_patties)
    except ValueError:
        print(
            "The data for number of patties must be an integer. Please double check the dataset."
        )
        SystemExit

    try:
        number_of_cheese_slices = int(number_of_cheese_slices)
    except ValueError:
        print(
            "The data for number of cheese slices must be an integer. Please double check the dataset."
        )
        SystemExit

    if has_tomato == "yes":
        has_tomato = True
    elif has_tomato == "no":
        has_tomato = False

    if has_lettuce == "yes":
        has_lettuce = True
    elif has_lettuce == "no":
        has_lettuce = False

    if has_onion == "yes":
        has_onion = True
    elif has_onion == "no":
        has_onion = False

    burger_order = (
        bun,
        sauce,
        number_of_patties,
        number_of_cheese_slices,
        has_tomato,
        has_lettuce,
        has_onion,
    )
    return burger_order
    # return None if error converting line to tuple


def get_cost(burger_order):
    """
    determine the cost of a burger via the burger order tuple passed in as a parameter
    return cost of burger as integer
    """
    (
        bun,
        sauce,
        number_of_patties,
        number_of_cheese_slices,
        has_tomato,
        has_lettuce,
        has_onion,
    ) = burger_order

    number_of_patties_list = [0, 1, 2, 3]

    number_of_cheese_slices_list = [0, 1, 2, 3]

    total_cost = 5

    # Check each ingredient input and increase the total cost accordingly if there is extra ingredients from the base burger
    if bun == "gluten free":
        total_cost += 1

    if number_of_patties not in number_of_patties_list:
        print(
            f"The number of patties is invalid for one of the burger order. The patties can only be one of these values: {number_of_patties_list}"
        )
        SystemExit

    if number_of_patties > 1:
        number_of_extra_patties = number_of_patties - 1
        total_cost = total_cost + (number_of_extra_patties * 3)

    if number_of_cheese_slices not in number_of_cheese_slices_list:
        print(
            f"The number of cheese slices is invalid for one of the burger order. The cheese slices can only be one of these values: {number_of_cheese_slices_list}"
        )
        SystemExit

    if number_of_cheese_slices > 1:
        number_of_extra_cheese_slices = number_of_cheese_slices - 1
        total_cost = total_cost + (number_of_extra_cheese_slices * 1)

    salad_choices = [has_tomato, has_lettuce, has_onion]

    if all(salad_choices):
        total_cost += 2
    elif salad_choices.count(True) == 2:
        total_cost += 1

    return total_cost


if __name__ == "__main__":
    main()
