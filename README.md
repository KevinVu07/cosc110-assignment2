# cosc110-assignment2

# Orders

A program to display top common orders for Codetown Burger Co.
Developed to fulfill the requirements of Programming Task 2 for COSC110, T1 2024.

## Usage

```bash
python3 orders.py
```

## Example interaction

```
Given the following contents in orders.txt:

milk,tomato,2,1,yes,no,no
milk,barbecue,3,3,yes,yes,yes
gluten free,barbecue,1,0,no,yes,no
milk,barbecue,3,3,yes,yes,yes
gluten free,barbecue,1,0,no,yes,no
milk,barbecue,3,3,yes,yes,yes
milk,barbecue,3,3,yes,yes,yes
milk,tomato,2,1,yes,no,no
an interaction with the program could look like:

How many of the top burger orders would you like to output? 2
The top burger orders were:
('milk', 'barbecue', 3, 3, True, True, True)    4   $15
('gluten free', 'barbecue', 1, 0, False, True, False)   2   $6
or:

How many of the top burger orders would you like to output? ok
Invalid value. Please enter a posiive integer
How many of the top burger orders would you like to output? -1
Invalid value. Please enter a positive integer
How many of the top burger orders would you like to output? 0
Invalid value. Please enter a positive integer
How many of the top burger orders would you like to output? 12
The top burger orders were:
('milk', 'barbecue', 3, 3, True, True, True)    4   $15
('gluten free', 'barbecue', 1, 0, False, True, False)   2   $6
('milk', 'tomato', 2, 1, True, False, False)    2   $8
Given the following contents of orders.txt:

hello
an interaction with the program could look like:

Error reading data.
Please ensure each line of orders.txt starts with the bun type (milk or gluten free), followed by a comma, then the sauce type (tomato, barbecue or none), followed by a comma, then the number of patties (0-3), followed by a comma, then the number of slices of cheese (0-3), followed by a comma, then whether tomato is included (yes or no), followed by a comma, then whether lettuce is included (yes or no), followed by a comma, then whether onion is included (yes or no).
```

## Contributors

Kevin Vu [hvu7@myune.edu.au]
