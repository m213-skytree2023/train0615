import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pic_class import PicInfo

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


pic_info_list = []

endpoint = "https://pixabay.com/api"

params = {
    "key": "37300172-0e10f824e72aee9244609aac2",
    "q": search,
    "lang": "ja",
    "image_type": "photo"
}

result = requests.get(endpoint, params=params, verify=False)
res = result.json()

for hit in res["hits"]:
    p = PicInfo(hit["pageURL"], hit["type"], hit["tags"], hit["previewURL"], hit["largeImageURL"],
                hit["downloads"], hit["likes"])

    pic_info_list.append(p)

print(pic_info_list[0].pic_url)
