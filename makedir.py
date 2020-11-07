# ファイル名に応じてフォルダ分けするプログラム
# ファイル名：[コンテスト名][コンテスト回数][難易度].py
# コンテスト名："ABC", "ARC", "AGC"の3種類ある
# [コンテスト回数]は，0埋めの3桁で表現される．
# ex) 1回目 -> "001", 21回目-> "021", 302回目->"302"
# [コンテスト名]に対応するフォルダがなかったら，そのフォルダを作成し，ファイルを移動する
# 対応するフォルダがあったら，そこに移動する
#　[コンテスト回数]に対応するフォルダがなかったら，そのフォルダを作成して，ファイルをそこに移動する
# あるなら，そこに移動する
# ディレクトリ構造
# .
# ├─ ABC ┬─ ABC001┬ABC001A.py
# │      ├─ ABC002├ABC001B.py
# │      └─ ...
# ├─ ARC ┬─ ARC001
# │      ├─ ARC002
# │      └─ ...
# └─ AGC ┬─ AGC001
#        ├─ AGC002
#        └─ ...

import os
L = ["ABC", "ARC", "AGC"]

os.chdir(r"C:\Users\ikehara\Desktop\AtCoder")
files = os.listdir()

for file in files:
    contest = file[:3]
    num = file[3:6]
    if(contest in L):
        print(file)
    # os.renames(file, contest + "\\" + contest + num + "\\" + file)
