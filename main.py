import datetime, time

project_data =	{
  "programming": 0
}

def start_tracker():
    name = input("What project are you working on?\n")
    start=datetime.datetime.now()
    timer_active = True

    user_input = ""
    while user_input != "stop":
        user_input = input("Let me know when you want to stop")
    end=datetime.datetime.now()
    time = end-start
    print(time)
    
    if name in project_data:
        project_data[name] += time
    else:
        project_data.update({name: time})
    print(project_data)




start_tracker()