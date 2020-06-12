#!/usr/bin/python3

# Скрипт для очистки старых файлов и пустых директорий, скрипт принимает первым аргументом количество дней, которое файл
# файл находится без модификаций, далее принимает директории для чистки (одна или множество)
# Работает на Linux и Windows

import os
import sys
import time

if len(sys.argv) < 2:
    print('Error, missing arguments! Usage is day(s) /path/to/dir/')
    exit(1)

days = int(sys.argv[1])
folders = []

for i in range(2, len(sys.argv)):
    folders.append(sys.argv[i])

total_deleted_size = 0
total_deleted_file = 0
total_deleted_dirs = 0

now_time = time.time()
age_time = now_time - 60 * 60 * 24 * days


# Delete file older then x days
def delete_old_files(folder):
    global total_deleted_file
    global total_deleted_size

    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)
            file_mod_time = os.path.getmtime(file_name)
            if file_mod_time < age_time:
                file_size = os.path.getsize(file_name)
                total_deleted_size += file_size
                total_deleted_file += 1
                os.remove(file_name)


# Delete empty folders
def delete_empty_dir(folder):
    global total_deleted_dirs
    counter_empty_folders = 0

    for path, dirs, files in os.walk(folder):
        if not dirs and not files:
            counter_empty_folders += 1
            total_deleted_dirs += 1
            os.rmdir(path)

    if counter_empty_folders > 0:
        delete_empty_dir(folder)


start_time = time.asctime()

for folder in folders:
    delete_old_files(folder)
    delete_empty_dir(folder)

finish_time = time.asctime()

print('---------------------------------------------------------')
print(f'Start time: {start_time}')
print(f'Total deleted size: {str(int(total_deleted_size / 1024 / 1024))}MB')
print(f'Total deleted files: {str(total_deleted_file)}')
print(f'Total deleted empty folders: {str(total_deleted_dirs)}')
print(f'Finish time: {finish_time}')
print('---------------------------------------------------------')