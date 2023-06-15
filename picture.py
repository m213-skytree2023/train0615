import requests
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



endpoint = "https://pixabay.com/api"

headers = {

}
params = {
    "key": "37300172-0e10f824e72aee9244609aac2",
    "q": "プログラミング",
    "lang": "ja",
    "image_type": "photo"
}

result = requests.get(endpoint, headers=headers, params=params,verify=False)

res = result.json()

print(res["total"])
for hit in res["hits"]:
    print("詳細URL：" + hit["pageURL"])
    print("イメージタイプ：" + hit["type"])
    print("カテゴリ：" + hit["tags"])
    print("プレビュー画像URL：" + hit["previewURL"])
    print("画像URL：" + hit["largeImageURL"])
    print("ダウンロード数：" + str(hit["downloads"]))
    print("お気に入り数：" + str(hit["likes"]))
    print("---------------------------")
