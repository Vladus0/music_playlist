import requests
import os
from dotenv import load_dotenv
import argparse
from tools import download_imgs, download_text


def get_artists(api_key, args):
    url = f"https://api.genius.com/artists/{args}/songs"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    songs = response.json()["response"]["songs"]
    for song_info in songs:
        title = song_info["title"]
        name = song_info["artist_names"]
        relationships_index = song_info["relationships_index_url"]
        image_url = song_info["header_image_thumbnail_url"]
        release_date = song_info["release_date_for_display"]
        print(f"Название: {title} \nМузыкант: {name} \nСсылка на текст: {relationships_index} \nСсылка на изображение: {image_url} \nДата выхода: {release_date} \n")
        download_text(songs)
        download_imgs(songs)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Функция находит артиста по id")
    parser.add_argument("--id", help="Введите id артиста с сайта GENIUS", type=str, default="16775")
    args = parser.parse_args()
    api_key = os.getenv("API_KEY")
    get_artists(api_key, args.id)


if __name__=="__main__":
    main()
