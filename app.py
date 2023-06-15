from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

### ルーティング定義

@app.route('/')
def toppage():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def graph_search():
    if request.method == 'POST':
        search = request.form.get("search")
        #graph_list=
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
