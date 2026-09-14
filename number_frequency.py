numbers = [10, 20, 10, 30, 20, 10, 40, 30]

checked = []

for number in numbers:
    if number not in checked:
        print(number, "appears", numbers.count(number), "times")
        checked.append(number)
