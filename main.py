import datetime, time, json

with open('project_data.json', 'r') as project_data:
    data=project_data.read()
        
project_data = json.loads(data)

def start_tracker():
    name = input("What project are you working on?\n")
    start=time.time()
    timer_active = True

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


start_tracker()