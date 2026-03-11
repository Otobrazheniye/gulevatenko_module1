# 0)C
def create_file(file_name: str) -> None:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("success add\n")

# 1)A

def add_file():
    report_name = input("Enter title:\n").strip()
    comment = add_to_file_input_comm()

    task_priority = add_to_file_validation_taskp(add_to_file_input_taskp())
    status = add_to_file_validation_status(add_to_file_input_status())

    task_id = get_next_id("protocol.txt")
    line = add_to_file_create_str(task_id, task_priority, report_name, status, comment)
    add_to_file("protocol.txt", line)
    

def add_to_file_input_taskp():
    task_priority = int(input("Please choose correct task priority: \n 1] High \n 2] Medium \n 3] Low \n\t").strip())
    return task_priority

def add_to_file_input_status():
    status = int(input("This task in progress? \n 1] New task \n 2] In progress \n 3] Finished").strip())
    return status

def add_to_file_input_comm():
    comment = input("Please add comment about this task: \n\t")
    return comment

def add_to_file_validation_taskp(task_priority:int):
       
    match task_priority:
        case 1:
            task_priority = "High"
        case 2: 
            task_priority = "Medium"
        case 3:
            task_priority = "Low"
        case _ :
            raise ValueError("Wrong input priority")
    return task_priority


def add_to_file_validation_status(status:int):
    if status == 1: 
        status = "New"
    elif status == 2:
        status = "In progress"
    elif status == 3:
        status = "Finished"
    else: 
        raise ValueError("Wrong status")
    return status



def add_to_file_create_str(task_id: int, task_priority: str, report_name: str, status: str, comment: str) -> str:
    return (
        f"ID: {task_id}\t"
        f"Task priority: {task_priority}\t"
        f"Status: {status}\t"
        f"Report Name: {report_name.strip()}\t"
        f"Comment: {comment.strip()}\n"
    )
    
def add_to_file(file_name, report_line):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(report_line)




# 2)R
def read_file_clasic(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("".join(lines))
    return lines

def read_file(file_name: str) -> str:
    read_file_clasic(file_name)
    action_presort()
    return


# 3)U

def update_file_input():
    task_value = None
    status_value = None
    name_value = None
    comment_value = None

    while True:
        user_choose = int(input("What are you want update/change? \n 1]Task Priority \n2]Status \n 3]Report Name \n4]Comment \n\t0]Finish"))
        match user_choose:
            case 1:
                task_value = add_to_file_input_taskp()
                task_value = add_to_file_validation_taskp(task_value)
            case 2:
                status_value = add_to_file_input_status()
                status_value = add_to_file_validation_status(status_value)
            case 3:
                name_value = input("Enter new value:\n").strip()
            case 4:
                comment_value = add_to_file_input_comm()
            case 0:
                break
            case _:
                print("Wrong choise")
                # print("Change is finished")
                # bchange_procces = False
    return task_value,status_value,name_value,comment_value

def update_show_search_result(file_dict):
    report_name = input("Please enter ->Report Name<- for update:\n").strip().lower()

    for item in file_dict:
        if item.get("Report Name", "").lower() == report_name:
            print(item)
            return report_name

    print("Not found")
    return None

def update_change_search_result(report_name,file_dict):
    updated_lines = []
    found = False

    for line in file_dict:
        if line.get("Report Name", "").lower() == report_name:
            task_value,status_value,name_value,comment_value = update_file_input()
            if task_value is not None:
                line["Task priority"] = task_value
            if name_value is not None:
                line["Report Name"] = name_value
            if status_value is not None:
                line["Status"] = status_value
            if comment_value is not None:
                line["Comment"] = comment_value
            found = True
        
            # updated_lines.append(line)
        line_str = add_to_file_create_str(
            int(line["ID"]),
            line["Task priority"],
            line["Report Name"],
            line["Status"],
            line["Comment"]
        )
        updated_lines.append(line_str)
    return updated_lines,found
    
def update_show_change_result(file_name,updated_lines,found):
    if found:
        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(updated_lines)
        print("Updated successfully")
    else:
        print("Report not found")

def update_file(file_name: str) -> None:
    tasks = dict_to_list(file_name)

    try:
        task_id = int(input("Enter task ID to update:\n").strip())
    except ValueError:
        print("Wrong ID")
        return

    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("Task not found")
        return

    field = int(input("Update:\n1] Title\n2] Description\n3] Priority\n4] Status\n0] Exit\n"))
    if field == 0:
        return

    if field == 1:
        task["Report Name"] = input("New title:\n").strip()
    elif field == 2:
        task["Comment"] = input("New description:\n").strip()
    elif field == 3:
        task["Task priority"] = add_to_file_validation_taskp(add_to_file_input_taskp())
    elif field == 4:
        task["Status"] = add_to_file_validation_status(add_to_file_input_status())
    else:
        print("Wrong choice")
        return

    with open(file_name, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(add_to_file_create_str(
                int(t.get("ID", 0)),
                t.get("Task priority", ""),
                t.get("Report Name", ""),
                t.get("Status", ""),
                t.get("Comment", "")
            ))

    print("Updated successfully")

    

def find_task_by_id(tasks: list[dict], task_id: int) -> dict | None:
    for t in tasks:
        if int(t.get("ID", -1)) == task_id:
            return t
    return None


# 4)D
def delete_file(file_name: str) -> None:
    tasks = dict_to_list(file_name)
    try:
        task_id = int(input("Enter task ID to delete:\n").strip())
    except ValueError:
        print("Wrong ID")
        return

    new_tasks = [t for t in tasks if int(t.get("ID", -1)) != task_id]
    if len(new_tasks) == len(tasks):
        print("Task not found")
        return

    with open(file_name, "w", encoding="utf-8") as f:
        for t in new_tasks:
            f.write(add_to_file_create_str(
                int(t.get("ID", 0)),
                t.get("Task priority", ""),
                t.get("Report Name", ""),
                t.get("Status", ""),
                t.get("Comment", "")
            ))
    print("Deleted successfully")


# ID
def get_next_id(file_name: str) -> int:
    tasks = dict_to_list(file_name)
    if not tasks:
        return 1
    ids = [int(t.get("ID", 0)) for t in tasks if t.get("ID")]
    return (max(ids) + 1) if ids else 1

# Search
def search_tasks(file_name: str) -> None:
    q = input("Enter search text:\n").strip().lower()
    tasks = dict_to_list(file_name)

    result = [
        t for t in tasks
        if q in t.get("Report Name", "").lower() or q in t.get("Comment", "").lower()
    ]

    if not result:
        print("Nothing found")
    else:
        print_tasks(result)

# File dict transform

def file_to_dict(line):
    result = {}
    parts = line.strip().split("\t")

    for part in parts:
        if ":" in part:
            key,value = part.split(":",1)
            result[key.strip()] = value.strip()
    return result

def dict_to_list(file_name):
    result = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    result.append(file_to_dict(line))
    except FileNotFoundError:
        pass
    return result

def file_dict_interface(file_name):
    file_dict = dict_to_list(file_name)
    for x in file_dict:
        print(x,"\n")
    

# sort report by task/ststus
def sort_by_priority(tasks: list[dict]) -> list[dict]:
    order = {"high": 0, "medium": 1, "low": 2}
    return sorted(tasks, key=lambda t: order.get(t.get("Task priority", "").lower(), 99))

def sort_by_status(tasks: list[dict]) -> list[dict]:
    order = {"new": 0, "in progress": 1, "finished": 2}
    return sorted(tasks, key=lambda t: order.get(t.get("Status", "").lower(), 99))
        
def print_tasks(tasks: list[dict]) -> None:
    for t in tasks:
        print(t, "\n")


def sort_file(file_name: str, mode: int) -> None:
    tasks = dict_to_list(file_name)

    if mode == 2:          
        tasks = sort_by_priority(tasks)
    elif mode == 3:        
        tasks = sort_by_status(tasks)
    else:
        return

    print_tasks(tasks)

def action_presort():
    user_choose = int(input("View:\n1] Original\n2] Sort priority\n3] Sort status\n4] Search\n0] Exit\n"))
    if user_choose == 1:
        print_tasks(dict_to_list("protocol.txt"))
    elif user_choose in (2, 3):
        sort_file("protocol.txt", user_choose)
    elif user_choose == 4:
        search_tasks("protocol.txt")

# switch logistic
def action_pre_start(user_choose:int):
    match user_choose:
        case 1:
            add_file()
        case 2:
            read_file("protocol.txt")
            
        case 3:
            update_file("protocol.txt")

        case 4:
            delete_file("protocol.txt")
        case _:
            print("Enter again, uncorrect vatiant")

            
# main
menu_process = True
while menu_process:
    
    user_choose = int(input("Please choose action: \n1] Create \t 2] Read \n3] Update \t 4] Delete \n"))
    action_pre_start(user_choose)



    

