new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Перенесли задачу task_005 из new_tasks в completed_tasks
completed_tasks.append(new_tasks.pop())

# Удалили задачу task_007 из new_tasks
new_tasks.remove('task_007')

# Теперь из списка new_tasks делаем последнюю таску приоритетной
last_task = new_tasks.pop()
new_tasks.insert(0, last_task)
print(new_tasks[0])

