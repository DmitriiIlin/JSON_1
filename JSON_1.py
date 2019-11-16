import json
import requests
import sys

"""
def Get_information_in_file():
    response=requests.get("https://jsonplaceholder.typicode.com/todos")
    with open("json_1.txt",'w') as json_file:
        json.dump(response.text,json_file,indent=2)
"""

def get_information_from_site():
    response=requests.get("https://jsonplaceholder.typicode.com/todos")
    result=json.loads(response.text)
    return result

def write_information_in_file(input_information):
    file=open("json_1.txt" , "w")
    file.write(str(input_information))
    file.close()

def base_structure_creater(data):
    base_structure={} 
    base_structure['userId']=data['userId']
    if data['title'] != 'None':
        base_structure['title']=1
    else:
        base_structure['title']=0
    if data['completed'] == True:
        base_structure['completed'] = 1
    else:
        base_structure['completed'] = 0
    return base_structure
    

def q_ty_of_users(input_information):
    write_information_in_file(input_information)
    list_for_work=input_information
    base_result = []
    idusers=[]
    base_structure={}
    for every_data in range(0 , len(list_for_work)):
        data = list_for_work[every_data]
        base_structure=base_structure_creater(data)
        if len(base_result) == 0:       
            base_result.append(base_structure)
        else:            
            if data['userId'] in idusers:
                base_result[data['userId']-1]['title'] = base_result[data['userId']-1]['title'] + base_structure['title']
                base_result[data['userId']-1]['completed'] = base_result[data['userId']-1]['completed'] + base_structure['completed']
            else:
                base_result.append(base_structure)  
        idusers.append(data['userId'])
    return base_result

"""            
print(q_ty_of_users(get_information_from_site()))
"""

