import os.path
import sys

mypath = sys.argv[1]
file_name = sorted([f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))])
start_index = sys.argv[2] if len(sys.argv) > 2 else 0
for i, old_name in enumerate(file_name):
    extension = ".".join(old_name.split('.')[1])
    n = start_index + i
    new_name = f'{n:04}'
    os.rename(mypath + os.path.sep + old_name, mypath + os.path.sep + new_name + extension)
