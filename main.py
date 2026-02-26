# Из чего состоит?
# Задача должна состоять из названия, описания, приоритета, статуса и уникального идентификатора.
# Приоритет может иметь три варианта: низкий, средний, высокий.
# Статус может иметь три варианта: новая, в процессе, завершена.
# Уникальный идентификатор (id) — это просто число, которое всегда на 1 больше, чем самое большое из уже существующих. Например, 
# если у вас задач нет, то для первой этот параметр будет равен 1. Если у вас уже есть задачи с номерами 1, 2, 3, то новая будет 
# создана с номером 4. 
# Если пользователь удалил несколько задач и у вас остались задачи 1, 3, 5, то следующая будет с номером 6.

#! CRUD 
# Task priority Name status comment ID(More->Details ) 
#! Data = text.txt in folder
#! Реализуйте пользовательский интерфейс (например, с помощью цикла while и ввода пользователя) для взаимодействия с системой задач.
# Добавьте возможность сортировки задач по приоритету или статусу при просмотре.
# Реализуйте возможность поиска задач по ключевым словам в названии или описании.




# 0)C
def create_file(file_name: str) -> None:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("success add\n")

# 1)A
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



def add_to_file_create_str(task_priority:str, report_name, status:str, comment):
    report_line = (
        f"Task priority: {task_priority}\t\t"
        f"Status: {status}\t\t"
        f"Report Name: {report_name.strip()}\t\t"
        f"Comment: {comment}\n"
        "\n"
    )
    return report_line
    
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
    return


# 3)U

def update_file_input():
    task_value = None
    status_value = None
    name_value = None
    comment_value = None
    bchange_procces = True

    # while bchange_procces:
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



def update_file(file_name: str) -> None:
    file_dict_interface(file_name)    
    file_dict =  dict_to_list(file_name)
    report_name = input("Please enter ->Report Name<- for update:\n").strip().lower()
    
    found_flag = False
    for sorted_name in file_dict:
        if sorted_name["Report Name"] == report_name:
            print(sorted_name)
            found_flag = True
            break
            
    if not found_flag:
            return print("Not found")

    updated_lines = []
    found = False

    for line in file_dict:
        if line["Report Name"].lower() == report_name:
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
            line["Task priority"],
            line["Report Name"],
            line["Status"],
            line["Comment"]
        )
        updated_lines.append(line_str)

    if found:
        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(updated_lines)
        print("Updated successfully")
    else:
        print("Report not found")


# 4)D
def delete_file(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("".join(lines))
    
    user_choose = input("Enter  what you want delete:")
    with open(file_name, "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip() != user_choose:
                f.write(line)
    # print("".join(line))



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
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                result.append(file_to_dict(line))
    return result 

def file_dict_interface(file_name):
    file_dict = dict_to_list(file_name)
    for x in file_dict:
        print(x,"\n")
    



def action_pre_start(user_choose:int):
    match user_choose:
        case 1:
            report_name = input("Please enter ->Report Name<-:\n").strip().lower()
            task_priority = add_to_file_input_taskp()
            status = add_to_file_input_status()
            comment = add_to_file_input_comm()
            task_priority = add_to_file_validation_taskp(task_priority)
            status = add_to_file_validation_status(status)
            line = add_to_file_create_str(task_priority, report_name, status, comment)
            add_to_file("protocol.txt", line)
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
    # result = dict_to_list("protocol.txt")
    # print(result)

    # file_dict_interface("protocol.txt")

    # res_dict = dict_to_list("protocol.txt")
    # print(res_dict)

    user_choose = int(input("Please choose action: \n1] Create \t 2] Read \n3]Update \t 4] Delete \n"))
    action_pre_start(user_choose)



    

