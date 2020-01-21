import datetime, time, json

with open('project_data.json', 'r') as project_data:
    data=project_data.read()
        
project_data = json.loads(data)

def start_tracker():
    name = input("What project are you working on?\n")
    start=time.time()
    print(datetime.datetime.now())
    timer_active = True
    print(start)

    user_input = ""
    while user_input != "stop":
        user_input = input("Let me know when you want to stop")
    end=time.time()
    elapsed_time = int(end-start)
    print(elapsed_time)
    
    if name in project_data:
        project_data[name] += elapsed_time
    else:
        project_data.update({name: elapsed_time})

    print(project_data)
    with open('project_data.json', 'w') as data_to_write:
        json.dump(project_data, data_to_write)

task = input("d for delete, s for start timer")
if task == "s":
    start_tracker()
elif task == "d":
    print(project_data)
    project_to_delete = input("which project do you want to delete?")
    if project_to_delete in project_data:
        project_data.pop(project_to_delete, None)
        with open('project_data.json', 'w') as data_to_write:
            json.dump(project_data, data_to_write)
    else:
        print("That doesn't exist")

