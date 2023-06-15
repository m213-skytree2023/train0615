import requests
API_KEY = '37300172-0e10f824e72aee9244609aac2'
BASE_URL = f'https://pixabay.com/api/?key={API_KEY}'
def search_images(keyword):

    api_endpoint = f'https://pixabay.com/api/photos?keyword={keyword}'
    response = requests.get(api_endpoint,verify=False)
    data = response.json()
    return data
def main():
    keyword = input("キーワードを入力してください: ")
    image_data = search_images(keyword)

    if image_data:
        print(f"{len(image_data)}の画像が見つかりました。")


        for image in image_data:
            print(image['url'])
    else:
        print("画像が見つかりませんでした。")

if __name__ == '__main__':
    main()

