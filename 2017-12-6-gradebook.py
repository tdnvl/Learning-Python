# Exercise 4 at https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/lists/exercises_list_and_dictionaries.html
results = []
lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]
# for i in students:
#    print(i["name"])
#    print(i["homework"])
#    print(i["quizzes"])
#    print(i["tests"])

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return (total / len(numbers))

def get_average(student):
    homework = average(student["homework"])
    quizzes= average(student["quizzes"])
    tests = average(student["tests"])
    return homework*.1 + quizzes*.3 + tests*.6

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return
    else:
        return "F"

for i in students:
    print(str(i["name"]) + "'s letter grade is: " + get_letter_grade(get_average(i)))

for i in students:
    print(i["name"] + "'s average is: " + str(get_average(i)))

def get_class_average(students):
    results = []
    for i in students:
        results.append(get_average(i))
        # print("The total of all averages is " + str(results))
    results = sum(results) / len(students)
    return results
# print("The length of students is " + str(len(students)))
class_average = get_class_average(students)

print("The class's average is: " + str(class_average))
print("The class's letter grade is: " + get_letter_grade(class_average))


