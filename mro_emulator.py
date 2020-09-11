from typing import List

"""
Эмулирует работу стандартного MRO в Python
"""

n_creations = int(input())
parent_dict = {}  # key - child, value - list of parents
for i in range(n_creations):
    one_cre_command: List[str] = input().strip().split()
    if ':' in one_cre_command:
        one_cre_command.remove(":")
    key = one_cre_command.pop(0)
    if key not in parent_dict.keys():
        parent_dict[key] = one_cre_command
    else:
        parent_dict[key].extend(one_cre_command)

#print("Прием данных закончен")
#print(parent_dict)

# прием запросов к базе
n_questions = int(input())
question = {}  # key - number of question, value - pair of possible [parent,child]
for i in range(n_questions):
    one_question: List[str] = input().strip().split()
    question[i] = one_question


# возвращает True если среди предков child_arg есть parent_arg
def is_child(child_arg: str, parent_arg: str) -> bool:
    if child_arg not in parent_dict.keys():
        return False
    if parent_dict[child_arg].__len__() == 0:
        return False
    elif parent_arg in parent_dict[child_arg]:
        return True
    else:
        for new_parent in parent_dict[child_arg]:  # вызываем поиск среди предков child_arg
            if is_child(new_parent, parent_arg):
                return True
    return False


# обработка запросов к базе
for i in range(n_questions):
    parent = question[i][0]
    child = question[i][1]
    if child == parent:
        print("Yes")
        continue
    if child not in parent_dict.keys():
        print("No")
        continue
    # ответим на вопрос: является ли child - дочерним классом parent
    if is_child(child, parent):
        print("Yes")
    else:
        print("No")

