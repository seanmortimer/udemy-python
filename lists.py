list = ["Bob", "Rolf", "Anne"]
tuple = ("Bob", "Rolf", "Anne")
set = {"Bob", "Rolf", "Anne"}

print(list[1])
print(tuple[1])

list.remove("Bob")

print(list)

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

print(set1.intersection(set2))

print(5 == 5)
print('Sean!')


# Destructring
person = ('Bob', 42, 'Mechanic')
name, _, proffession = person

print(name, proffession)

ha, *ta = [1, 2, 3, 4, 5]

print(ha)
print(ta)