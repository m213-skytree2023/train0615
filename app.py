from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
from pic_class import PicInfo
from requests.packages.urllib3.exceptions import InsecureRequestWarning
app = Flask(__name__)

### ルーティング定義

@app.route('/')
def toppage():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def graph_search():
    if request.method == 'POST':
        search = request.form.get("search")
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

    return render_template('searchResult.html',graph_list=pic_info_list,search=search)




if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
