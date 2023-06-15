from flask import Flask, render_template, request, redirect, url_for, flash, session
from pic_class import PicInfo

app = Flask(__name__)

### ルーティング定義

@app.route('/')
def toppage():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def graph_search():
    if request.method == 'POST':
        search = request.form.get("search")
        graph_list= []
        g = PicInfo("111111", "picture_type", "categories", "preview_url", "https://pixabay.com/get/gd52d02f4eb1ba4c4126e040589756f0913796caee666a72ce9f8697cc35965ec75a337f1e9dec6c852ac94f6f955f16607f6dc703b4c381275752d3ce79f2b1b_640.jpg", 123, 456)
        graph_list.append(g)
    return render_template('searchResult.html',search = search, graph_list = graph_list)




if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
