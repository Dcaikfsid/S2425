from student import Student

budnychenko = Student("Denys", 15.7, "S2816", 120.0)
solop = Student("Illya", 16.1, "S2816", 105.0)
oliynyk = Student("Kostya", 14.2, "S2816", 1200.0)
students = []
students.append(budnychenko)
students.append(solop)
students.append(oliynyk)
for student in students:
    student.String()
iphone15price = 1000
budnychenko.Buy(iphone15price)
solop.Buy(iphone15price)
oliynyk.Buy(iphone15price)
for student in students:
    student.String()
e)
days = 365
for day in days:
    