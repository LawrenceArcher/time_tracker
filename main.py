import datetime, time

project_data =	{
  "programming": 0
}
print(time.clock())
print(time.time())
def start_tracker():
    name = input("What project are you working on?\n")
    start=time.time()
    timer_active = True

    user_input = ""
    while user_input != "stop":
        user_input = input("Let me know when you want to stop")
    end=time.time()
    elapsed_time = end-start
    print(elapsed_time)
    
    if name in project_data:
        project_data[name] += elapsed_time
    else:
        project_data.update({name: elapsed_time})
    print(project_data)




start_tracker()