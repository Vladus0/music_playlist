import requests
import os
from dotenv import load_dotenv
import argparse
from tools import download_imgs, download_text


def get_songs_info_id(api_key, args):
    url = f"https://api.genius.com/songs/{args}"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    song = response.json()["response"]["song"]
    artist_name = song["artist_names"]
    song_title = song["title"]
    song_url = song["url"]
    song_img = song["header_image_thumbnail_url"]
    song_date = song["release_date_for_display"]
    print(f"Название: {song_title} \nМузыкант: {artist_name} \nСсылка на текст: {song_url} \nСсылка на изображение: {song_img} \nДата выхода: {song_date} \n")
    download_imgs(song)
    download_imgs(song)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Функция находит песню по id")
    parser.add_argument("--id", help="Введите id песни с сайта GENIUS", default="378195")
    args = parser.parse_args()
    api_key = os.getenv("API_KEY")
    get_songs_info_id(api_key, args.id)


if __name__=="__main__":
    main()