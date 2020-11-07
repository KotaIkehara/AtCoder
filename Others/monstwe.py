import requests
import json


def main():
    # read file
    monsters = ["dragon", "griffin", "medusa", "troll", "vampire"]
    api = "https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/{monster1}+{monster2}"

    score = {"dragon": 0, "griffin": 0, "medusa": 0, "troll": 0, "vampire": 0}
    for i, name in enumerate(monsters[:-1]):
        for j in range(i + 1, len(monsters)):
            # APIのURLを得る
            url = api.format(monster1=name, monster2=monsters[j])
            # 実際にAPIにリクエストを送信して結果を取得する
            r = requests.get(url)
            # 結果はJSON形式なのでデコードする
            data = json.loads(r.text)
            score[data["winner"]] += 1
    ans = sorted(score.items(), key=lambda x: -x[1])
    for i in range(len(ans)):
        print(ans[i][0][0])


main()
