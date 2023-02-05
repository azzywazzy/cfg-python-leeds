# with open("todo.txt", "r") as text_file:
#     contents = text_file.read()

# print(contents)


new_item = input("What shall I add to my to do list? ")

with open("todo.txt", "r") as text_file:
    contents = text_file.read()

with open("todo.txt", "w+") as text_file:
    updated = contents.append(new_item)
    text_file.write(updated)

print(contents)