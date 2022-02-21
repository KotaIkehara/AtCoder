import glob
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def read_data(filename):
    result = []
    f = open(filename, "r")
    line = f.readline()

    alpha = 1
    while line:
        words = line[:-1].split(" ")
        if words[0] == "Ave.":
            result.append(words[2:])
            alpha += 1
        line = f.readline()

    while alpha <= 9:
        result.append(["0", "-", "-"])
        alpha += 1
    return result


### スプレッドシートへのアクセス ###
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    './spread-326805-33e183eaecc9.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('sample').sheet1
### スプレッドシートへのアクセス ###


# シートへの書き込み ###
mtx_name = "G3_circuit"
# ファイルの取得
sciccg_file, diccg_file = glob.glob('./data/'+mtx_name+'.sh.*')

### スプレッドシートのヘッダ位置を検索 ###
cell = wks.find(mtx_name)
row, col = cell.row, cell.col

# SCICCGの結果
result = read_data(sciccg_file)
start = "R" + str(row+3) + "C" + str(col)
end = "R" + str(row+11) + "C" + str(col+2)
wks.update(start+":"+end, result)

# DICCGの結果
result = read_data(diccg_file)
start = "R" + str(row+12) + "C" + str(col)
end = "R" + str(row+20) + "C" + str(col+2)
wks.update(start+":"+end, result)
