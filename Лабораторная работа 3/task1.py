src = not False and True or False and not True

# result = True and True or False and False # убрала отрицания
# result = True or False # убрала логическое "И"
# result = True # убрала логическое "ИЛИ"

result = True

print(src == result)
