import requests

def read(auth_params, base_url, board_id):
    #Get information about board's column
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params = auth_params).json()

    #Go along massive
    for column in column_data:
        #Get information about each task in column
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params = auth_params).json()
        print(column['name'],' ', len(task_data))
        if not task_data:
            print('\t' + 'No tasks!')
            continue
        for task in task_data:
            print('\t' + task['name'])

    return 1


def create_task(name, column_name,auth_params, base_url, board_id):
    #Get information about board's column
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params = auth_params).json()

    #Find correct field in column
    for column in column_data:
        if column['name'] == column_name:
            #POST your param and add your task
            requests.post(base_url.format('cards'), data={'name': name, 'idList':column['id'], **auth_params})
            break
    return 1

def create_column(name,auth_params, base_url, board_id):
    #POST information and add column to board
    requests.post(base_url.format('boards') + "/" + board_id + "/lists", data={'name': name, **auth_params})

    return 1



def move(name, column_name,auth_params, base_url, board_id):
    #Get information about board's column
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

    #Create list where programm put equal name of tasks
    tasks=[]
    info = "Found >1 tasks! Please choose what's you mean\n"

    count = 0
    for column in column_data:
        column_task = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        for task in column_task:

            # add equal tasks
            if task['name'] == name:
                count += 1
                info += str(count) + ". " + str(task['id']) + " - task_id in " + column['name'] + "\n"
                tasks.append(task['id'])

    #simple handler
    if(len(tasks) == 0):
        print('\t'+'task not found')
        return 1
    elif len(tasks) == 1:
        task_id = tasks[0]
    else:
        #If programm find more than 1 equal task's name then it ask you to choose correct task
        print(info)
        task_id = tasks[int(input()) - 1]



    #change task location
    for column in column_data:
        if column['name']==column_name:
            #
            requests.put(base_url.format('cards') + '/' + task_id +
                         '/idList',  data={'value':column['id'],
                                           **auth_params})
            break

    return 1

def main():
    #ask base information for work
    base_url = "https://api.trello.com/1/{}"
    key = input("Enter your trello key")
    token = input("Enter your trello token")
    board_id = input("Enter board id")
    auth_params = {
        'key':key,
        'token':token
    }
    decide = 1
    while decide:
        print("What do you want?")
        print("Enter 1 to show board")
        print("Enter 2 to create new task in column")
        print("Enter 3 to create new column")
        print("Enter 4 to move task to another column")
        print("Enter 0 to exit")
        decide = input()
        if decide == "1":
            read(auth_params, base_url, board_id)
        elif decide == "2":
            create_task(
                input("Enter name of task"),
                input("Enter name of column(Where you add new task)"),
                auth_params, base_url, board_id
            )
        elif decide == "3":
            create_column(
                input("Enter name of column"),
                auth_params, base_url, board_id
            ),
        elif decide == "4":
            move(
                input("Enter name of task"),
                input("Enter name of column"),
                auth_params, base_url, board_id
            )
        elif decide == "0":
            break
        else:
            print("Please, enter 0, 1, 2, 3 or 4")



if __name__ == "__main__":
    main()