project_data =	{"programming": 1}

def add_new_entry():
    time = 5
    name = str(input("project?\n"))
    
    increment = {name: time}
    print(increment)
    print({name, time})
    if name in project_data:
        project_data[name] += time
    else:
        project_data.update(increment)


add_new_entry()

# new_data = {"music": 5}
# project_data.update(new_data)

print(project_data)

# d = {1: "one", 2: "three"}
# d1 = {2: "two"}

# # updates the value of key 2
# d.update(d1)
# print(d)

# d1 = {3: "three"}

# # adds element with key 3
# d.update(d1)
# print(d)