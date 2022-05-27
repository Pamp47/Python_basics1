from os import mkdir
from os.path import join, exists

fix_name = "task_1"
main_dir = "my_project"
sub_dirs = ["settings", "mainapp", "adminapp", "authapp"]
main_path = join(".", fix_name, main_dir)
if not exists(main_path): mkdir(main_path)

for sub_dir in sub_dirs:
    sub_path = join(".", fix_name, main_dir, sub_dir)
    if not exists(sub_path): mkdir(sub_path)
