import os
import sys
import glob
import time

def get_recently_contest_path():
    current_dir = os.getcwd()
    contest_dir = os.path.join(current_dir, "contest")

    dir_list = []
    for name in glob.glob(f"{contest_dir}/abc*"):
        contest_num = int(name[-3:])
        dir_list.append(contest_num)

    recently_contest_num = max(dir_list)
    recently_contest_dir = os.path.join(current_dir, "contest", f"abc{recently_contest_num}")
    return recently_contest_dir

def exec(args):
    recently_contest_dir = get_recently_contest_path()

    exec_question = args[1]
    exec_file = os.path.join(recently_contest_dir, f"{exec_question}.py")
    exec_input_file = os.path.join(recently_contest_dir, f"{exec_question}.txt")

    print("-----------------------")
    start_time = time.perf_counter()
    os.system(f"python {exec_file} < {exec_input_file}")
    end_time = time.perf_counter()
    time_diff = round((end_time - start_time) * 1000, 4)
    print(f"\nexec_time: {time_diff}ms")
    print("-----------------------")

args = sys.argv
exec(args)