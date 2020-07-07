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
name1, _, proffession = person

print(name1, proffession)

ha, *ta = [1, 2, 3, 4, 5]

print(ha)
print(ta)

# Dictionary comprehensions

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

print(student['school'])

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =  data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, 
# for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count

