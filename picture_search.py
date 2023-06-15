import requests
def perform_image_search(search):
    search = requests.form.get("search")
    pic_data = response.json()
    if pic_data:
        pic_info_list = []

        for pic in res :

                api_url = pic['pageURL']
                picture_type = pic.get('type', '')
                categories = pic.get('tags', '').split(', ')
                preview_url = pic.get('previewURL', '')
                pic_url = pic.get('webformatURL', '')
                download_count = pic.get('downloads', 0)
                favorites = pic.get('favorites', 0)

                pic_info = PicInfo(api_url, picture_type, categories, preview_url, pic_url, download_count, favorites)
                pic_info_list.append(pic_info)