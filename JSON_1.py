import json
import requests
import sys

"""
def Get_information_in_file():
    response=requests.get("https://jsonplaceholder.typicode.com/todos")
    with open("json_1.txt",'w') as json_file:
        json.dump(response.text,json_file,indent=2)
"""

def Get_information_from_site():
    response=requests.get("https://jsonplaceholder.typicode.com/todos")
    result=json.loads(response.text)
    return result

def Write_information_in_file(input_information):
    file=open("json_1.txt" , "w")
    file.write(str(input_information))
    file.close()

def Q_ty_of_users(input_information):
    Write_information_in_file(input_information)
    list_for_work=input_information
    users = []
    every_user_tasks = []
    complited_task = []
    uncomplited_task = []
    result = []
    base_structure={}
    for every_data in range(0 , len(list_for_work)):
        data = list_for_work[every_data]
        if data["userId"] not in users:
            users.append(data["userId"])
            every_user_tasks.append([])
            complited_task.append([])
            uncomplited_task.append([])
    for every_user in range(0 , len(users)):
        for i in range(0 , len(list_for_work)):
            data=list_for_work[i]
            if users[every_user]==data["userId"]:
                if data["title"] not in every_user_tasks[every_user]:  
                    every_user_tasks[every_user].append(data["title"])
                    if data["completed"] == True:
                        complited_task[every_user].append("True")
                    else:
                        uncomplited_task[every_user].append("False")
    for j in range(0 , len(users)):
        base_structure=dict(userId = users[j],title = every_user_tasks[j],completed = len(complited_task[j]))
        result.append(base_structure)
    return result
    
    


"""

print(Q_ty_of_users(Get_information_from_site()))

"""
