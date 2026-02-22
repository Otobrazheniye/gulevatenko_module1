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
def add_to_file_input():
    task_priority = int(input("Please choose correct task priority: \n 1] High \n 2] Medium \n 3] Low \n\t").strip())
    status = int(input("This task in progress? \n 1] No \n 2] Yes \n").strip())
    return task_priority, status

def add_to_file_input_comm():
    comment = input("Please add comment about this task: \n\t")
    return comment

def add_to_file_validation(task_priority:int, status:int):
       
    match task_priority:
        case 1:
            task_priority = "High"
        case 2: 
            task_priority = "Medium"
        case 3:
            task_priority = "Low"
        case _ :
            raise ValueError("Wrong input priority")


    if status == 1: 
        status = "New"
    elif status == 2:
        status = "In progress"
    else: 
        raise ValueError("Wrong status")
    return task_priority,status

def add_to_file_create_str(task_priority:str, report_name, status:str, comment):
    report_line = (
        f"Task priority: {task_priority}\t\t"
        f"Report Name: {report_name.strip()}\t\t"
        f"Status: {status}\t\t"
        f"Comment: {comment}\n"
        "\n"
    )
    return report_line
    
# Task priority Name status comment ID(More->Details ) 
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
    

    # report_name = input("Please enter ->Report Name<-:\n").strip().lower()

    # if report_name + "\n" in lines or report_name in [ln.strip() for ln in lines]:
    #     print("found")
    # else:
    #     print("not found")

    # return "".join(lines)
    return


# 3)U


def update_file(file_name: str) -> None:
    lines = read_file_clasic(file_name)

    report_name = input("Please enter ->Report Name<- for update:\n").strip().lower()
    new_value = input("Enter new value:\n").strip()

    updated_lines = []
    found = False

    for line in lines:
        if line.strip().lower() == report_name:
            updated_lines.append(new_value + "\n")
            found = True
        else:
            updated_lines.append(line)

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



def action_pre_start(user_choose:int):
    match user_choose:
        case 1:
            report_name = input("Please enter ->Report Name<-:\n").strip().lower()
            task_priority, status = add_to_file_input()
            comment = add_to_file_input_comm()
            task_priority, status = add_to_file_validation(task_priority,status)
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


# main
menu_process = True
while menu_process:
    # result = parse_file("protocol.txt")
    # print(result)

    res_dict = dict_to_list("protocol.txt")
    print(res_dict)

    user_choose = int(input("Please choose action: \n1] Create \t 2] Read \n3]Update \t 4] Delete \n"))
    action_pre_start(user_choose)



    

