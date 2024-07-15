# kvtz1 = open('requirements.txt', 'a')
# kvtz1.writelines(input("enter new dependency: "))
#
# kvtz1.close()
#
# kvtz = open('requirements.txt', 'r')
# for line in kvtz.readlines():
#     print(f'Current dep is "{line}"', end='')

# Create an empty list to store the names
# names = []
#
# # Get names from user using a for loop
# for i in range(1,4):
#     name = input(f"Enter name {i}: ")
#     names.append(name)
#
# # Write names to a file
# with open("names.txt", "w") as file:
#     for name in names:
#         file.writelines(name)
#
# with open("names.txt", "r") as file:
#     for name in file.read():
#         print(f"hello {name}\n")
#
#
# print("Names written to names.txt file.")

# Step 1: Accept three names as input
names = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    names.append(name + '\n')

# Step 2: Write the names to a text file using writelines
with open('names.txt', 'w') as file:
    file.writelines(names)

# Step 3: Read the names from the text file
with open('names.txt', 'r') as file:
    for line in file:
        print(f"Hello {line.strip()}")
