import os
import sys

PROBLEM_NAMES = ["A", "B", "C", "D", "E", "F"]

def create_file(dir_path):
    for problem in PROBLEM_NAMES:
        py_file_path = os.path.join(dir_path, f"{problem}.py")
        txt_file_path = os.path.join(dir_path, f"{problem}.txt")
        with open(py_file_path, "w") as py_file:
            py_file.write(f"# {problem}.py\n")
        with open(txt_file_path, "w") as txt_file:
            txt_file.write(f"{problem}.txt\n")

def create_contest(args):
    pwd_path = os.path.abspath(os.getcwd())
    dir_path = os.path.join(pwd_path, "contest", f"abc{args[1]}")
    os.makedirs(dir_path, exist_ok=True)
    create_file(dir_path)
    print(dir_path)

args = sys.argv
create_contest(args)