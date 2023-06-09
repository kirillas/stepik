"""Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре
все директории, в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий,
отсортированных в лексикографическом """
import os
import re

# p - текущий каталог
# d - список каталогов
# f - список файлов
arr = []
for (p, d, f) in os.walk("main"):
    for cur_file in f:
        if re.search(r"\.py", cur_file) != None:
            arr.append(p)

arr = list(set(arr))
arr.sort()
with open("2.4-main.txt", "w") as file_out:
    for dir_line in arr:
        file_out.write(dir_line + "\n")
