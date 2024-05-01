import os
import fileinput
import sys
import tkinter as tk
from tkinter import filedialog
import string
from tkinter import messagebox

# 选择文件路径
root = tk.Tk()
root.withdraw()
f_path = filedialog.askdirectory()

# 查找文件
find_folder_path = f_path
need_file_name = "savetoken.py"

threefile = os.path.abspath(os.path.join(find_folder_path, need_file_name))

# 新建txt文件
open('savetoken.txt', 'w')

# 复制内容到txt
read_file = open(threefile, 'r')
write_file = open('savetoken.txt', 'w')
r = read_file.read()
w = write_file.write(r)
read_file.close()
write_file.close()


# 查找匹配字符串所在行数
def find_string_line(file_path, target_string):
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if target_string in line:
                return line_num
    return -1


file_path = 'savetoken.txt'
target_string = 'def verify_data(data, signatures, check_verifying=True):'
line_num = find_string_line(file_path, target_string)


# 替换文本内容
def replace_line(file_path, line_number, new_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines[line_number - 1] = new_text + '\n'
    with open(file_path, 'w') as file:
        file.writelines(lines)


file_line_num = line_num + 22
replace_line('savetoken.txt', file_line_num, '    return True')

# 替换py文件
# 复制内容到py
new_read_file = open('savetoken.txt', 'r')
new_write_file = open(threefile, 'w')
new_r = new_read_file.read()
new_w = new_write_file.write(new_r)
new_read_file.close()
new_write_file.close()

# 删除txt文件
os.remove('savetoken.txt')

# 提示
messagebox.showinfo("完成", "文件修复完成!")
