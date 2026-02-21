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

#input:  {task_priority: _, status: _} {comment:_}
# validation
# create string
# f.write(line)

# Task priority Name status comment ID(More->Details ) 
def add_to_file(file_name:str,report_name):
    task_priority = int(input("Please choose correct task priority: \n 1] High \n 2] Medium \n 3] Low \n\t").strip())

    match task_priority:
        case 1:
            task_priority = "High"
        case 2: 
            task_priority = "Medium"
        case 3:
            task_priority = "Low"
        case _ :
            return print("Wrong input priority")
        
    status = int(input("This task in progress? \n 1] No \n 2] Yes \n").strip())
    if status == 1: 
        status = "New"
    elif status == 2:
        status = "In progress"
    else: 
        return print("Wrong information")

    comment = input("Please add comment about this task: \n\t")

  
    with open(file_name, "a", encoding="utf-8") as f:
        line = (
            f"Task priority: {task_priority}\t"
            f"Report Name: {report_name.strip()}\t"
            f"Status: {status}\t"
            f"Comment: {comment}\n"
            "-----\n"
        )
        f.write(line)
# 2)R
def read_file(file_name: str) -> str:
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("".join(lines))

    report_name = input("Please enter ->Report Name<-:\n").strip().lower()

    if report_name + "\n" in lines or report_name in [ln.strip() for ln in lines]:
        print("found")
    else:
        print("not found")

    return "".join(lines)

# 3)U
def update_file(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    print("".join(lines))

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
            add_to_file("protocol.txt",report_name)
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
    user_choose = int(input("Please choose action: \n1] Create \t 2] Read \n3]Update \t 4] Delete \n"))
    action_pre_start(user_choose)
    

