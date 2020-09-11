"""
Имитирует обработчик пространств имен в интерпретаторе Python
"""
# parent: key - child namespace, value - parent namespace
parent = {'global':'None'}
#varaibles: key - namespace, value - varaibles list
varaibles = {'global':[]}
while True:
    comm, nameS, arg = input().split()
    if comm == "create":
        parent[nameS]=arg
        varaibles[nameS]=[]
    elif comm =="add":
        varaibles[nameS].append(arg)
    elif comm =="get":
        curNameSpace = nameS
        while True:
            if curNameSpace == "None":
                print("None")
                break
            if arg in varaibles[curNameSpace]:
                print(curNameSpace)
                break
            else:
                curNameSpace = parent[curNameSpace]
    elif comm =='show':
        print(parent)
        print(varaibles)
