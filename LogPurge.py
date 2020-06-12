#!/usr/bin/python3

# Скрипт для очистки лог-файлов, скрипт принимает 3 аргумента: название файла, размер файла (в килобайтах) и необходимое количество копий старых логов.
# Работает на Linux и Windows

import shutil
import os
import sys

if len(sys.argv) < 4:
    print('Error, missing arguments! Usage is fileName fileSize fileCount')
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_count = int(sys.argv[3])

if os.path.isfile(file_name):
    logfile_size = os.stat(file_name).st_size
    logfile_size /= 1024

    if logfile_size >= limit_size:
        if logs_count > 0:
            for current_file_num in range(logs_count, 1, -1):
                src = file_name + '_' + str(current_file_num - 1)
                dst = file_name + '_' + str(current_file_num)
                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print(f'Copied {src} to {dst}')

            shutil.copyfile(file_name, file_name + '_1')
            print(f'Copied {file_name} to {file_name}_1')
        my_file = open(file_name, 'w')
        my_file.close()