username = input("Введите имя пользователя: ")
title = input("Введите заговловок заметки: ")
content = input("Напишите заметку: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки: ")
issue_date = input("Введите дату выполнения заметки: ")

print(username)
print(title)
print(content)
print(status)
print(created_date[:5])
print(issue_date[:5])