import requests
import os
from dotenv import load_dotenv
import argparse
from tools import download_imgs, download_text


def get_songs_name(api_key, args):
    url = "https://api.genius.com/search?q="
    headers = {
    "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "q": args
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    song = response.json()["response"]["hits"][0]["result"]
    artist_name = song["artist_names"]
    song_title = song["full_title"]
    song_url = song["url"]
    song_img = song["header_image_thumbnail_url"]
    song_date = song["release_date_for_display"]
    print(f"Название: {song_title} \nМузыкант: {artist_name} \nСсылка на текст: {song_url} \nСсылка на изображение: {song_img} \nДата выхода: {song_date} \n")
    download_text(song)
    download_imgs(song)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Функция находит песню по названию")
    parser.add_argument("--name", help="Введите название песни", default="Chandelier")
    args = parser.parse_args()
    api_key = os.getenv("API_KEY")
    get_songs_name(api_key, args.name)


if __name__=="__main__":
    main()