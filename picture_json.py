import requests



    def display(self):
        print("詳細URL:", self.api_url)
        print("イメージタイプ:", self.picture_type)
        print("カテゴリ:", ", ".join(self.categories))
        print("プレビュー画像URL:", self.preview_url)
        print("画像URL:", self.pic_url)
        print("ダウンロード数:", self.download_count)
        print("お気に入り数:", self.favorites)

def search_pic(search):
    api_endpoint = f'https://pixabay.com/api/photos?keyword={search}'
    response = requests.get(api_endpoint)
    data = response.json()
    return data


pic_data = search_pic(search)

if pic_data:
    print(f"{len(pic_data)}件の画像が見つかりました。")

    for pic in pic_data:
        if 'url' in pic:
            api_url = pic['pageURL']
            picture_type = pic.get('type', '')
            categories = pic.get('categories', '').split(', ')
            preview_url = pic.get('previewURL', '')
            pic_url = pic.get('pictureURL', '')
            download_count = pic.get('downloads', 0)
            favorites = pic.get('favorites', 0)

            pic_info = PicInfo(api_url, picture_type, categories, preview_url, pic_url, download_count, favorites)
            pic_info.display()
            print()  # フォーマットのための空行を出力
        else:
            print("画像のURLが見つかりません。")
else:
    print("画像が見つかりませんでした。")
