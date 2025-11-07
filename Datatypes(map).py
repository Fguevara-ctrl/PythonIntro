my_first_person = {
    "first_name": "Frank",
    "last_name": "Guevara",
    "age": 35,
    "is_happy": True,
    "Enemies": [None]
}

# print(my_first_person["last_name"], my_first_person["age"])

my_second_person = {
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 28,
    "is_happy": False,
    "Enemies": [my_first_person]
}

my_first_list = [my_first_person, my_second_person]

print(my_first_list[1]["Enemies"][0]["first_name"])