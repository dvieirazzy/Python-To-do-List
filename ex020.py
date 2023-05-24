import json
import os


def tolist(tasks):
    if not tasks:
        print('\nEmpty List')
        return
    print('\n----- TASKS -----')
    for i in tasks:
        print(f'✅ {i}')


def undo(tasks, taskHistoric):
    if not tasks:
        print('\nNothing to Undo')
        return
    task = tasks.pop()
    taskHistoric.append(task)
    tolist(tasks)


def redo(tasks, taskHistoric):
    if not taskHistoric:
        print('\nNothing to Redo')
        return
    task = taskHistoric.pop()
    tasks.append(task)
    tolist(tasks)


def add(task, tasks):
    if not task:
        print('\nEmpty Field')
        return
    tasks.append(task)
    tolist(tasks)


def loadjson(tasks, source):
    data = []
    try:
        with open(source, 'r', encoding='utf8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('\n- File Created')
        savejson(tasks, source)
    return data


def savejson(tasks, source):
    data = tasks
    with open(source, 'w', encoding='utf8') as file:
        data = json.dump(tasks, file, indent=2, ensure_ascii=False)
    return data


SOURCE = 'ex020.json'
tasks = loadjson([], SOURCE)
tasksHistoric = []

while True:
    print('\nTo Do List')
    print('[l]ist [u]ndo [r]edo [c]lear')
    task = input('Type a Task: ').strip()

    if task == 'l':
        tolist(tasks)
    elif task == 'u':
        undo(tasks, tasksHistoric)
    elif task == 'r':
        redo(tasks, tasksHistoric)
    elif task == 'c':
        os.system('cls')
    else:
        add(task, tasks)
    savejson(tasks, SOURCE)
