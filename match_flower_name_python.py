# Write your code here
flower_dic = {}
flower_file = open("flowers.txt")
# HINT: create a dictionary from flowers.txt
for line in flower_file:
    flower_dic[line[0]] = line[3:].strip()
# HINT: create a function to ask for user's first and last name
def ask_name():
    return input("What is your name?")
name = ask_name().upper()
# print the desired output
print("You are a {}!".format(flower_dic[name[0]]))