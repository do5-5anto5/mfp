#Type hints do not force the parameter or output type. They are useful as 
# indicators of what should happen in the function.

def calc_average(values: list) -> float:
    return sum(values) / len(values)


list1 = [1, 2, 3, 4, 5]
list2 = [45, 74, 50, 99, 51]
list3 = [548, 781, 961, 473, 552]

list4 = "Jonathan"

print(calc_average(list1))
print(calc_average(list2))
print(calc_average(list3))
print(calc_average(list4))

