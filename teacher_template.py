# get and process input for a list of names
names = input("Enter names separated by comas:").title().split(",")
# get and process input for a list of the number of assignments
assignments = input("Enter not done assignments count separated by comas:").split(",")
# get and process input for a list of grades
grades = input("Enter grades separated by comas:").split(",")

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for n, a, g in zip(names, assignments, grades):
	print(message.format(n, a, g, (int(a) * 2) + int(g)))

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
