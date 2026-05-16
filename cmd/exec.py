import os
import sys
import glob
import time
import tempfile

def get_recently_contest_path():
    # ターミナルを開いた時のディレクトリパスを取得
    current_dir = os.getcwd()
    contest_dir = os.path.join(current_dir, "contest")

    # 全てのフォルダ名を検索して最新のコンテストディレクトリパスを記録
    dir_list = []
    for name in glob.glob(f"{contest_dir}/abc*"):
        contest_num = int(name[-3:])
        dir_list.append(contest_num)

    recently_contest_num = max(dir_list)
    recently_contest_dir = os.path.join(current_dir, "contest", f"abc{recently_contest_num}")
    return recently_contest_dir

def exec_programs(exec_file, exec_program_path):
    # 実行時間計測開始
    start_time = time.perf_counter()

    # 入力例一時ファイルを使用しプログラム実行
    os.system(f"python {exec_file} < {exec_program_path}")

    # 実行時間計測終了・差分表示
    end_time = time.perf_counter()
    time_diff = round((end_time - start_time) * 1000, 4)
    print(f"\nexec_time: {time_diff}ms")
    print("-----------------------")

    # 入力例一時ファイルの削除
    os.remove(exec_program_path)

def exec(args):
    # 最新のコンテストディレクトリパスの取得
    recently_contest_dir = get_recently_contest_path()

    # 実行する問題とプログラムファイルパス・入力例パスを取得
    exec_question = args[1]
    exec_file = os.path.join(recently_contest_dir, f"{exec_question}.py")
    exec_input_file = os.path.join(recently_contest_dir, f"{exec_question}.txt")

    # ファイルを全て読み、¥n¥n¥nにて他入力例があったことを認識して分割
    with open(exec_input_file, "r") as f:
        content = f.read()
    input_part = content.split("\n\n\n")

    # 入力例を正規化し入力例一時ファイルに書き起こす
    for i, pattern in enumerate(input_part, 1):
        text = pattern.rstrip() + "\n"

        if text == "\n":
            continue

        with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as tf:
            tf.write(text)
            tf_name = tf.name

        # プログラムの実行
        exec_programs(exec_file, tf_name)

args = sys.argv
exec(args)