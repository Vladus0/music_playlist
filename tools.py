import requests
import os
from bs4 import BeautifulSoup


def download_imgs(songs):
    for song_info in songs:
        folder_path = f"songs/{song_info["artist_names"]}/images/"
        os.makedirs(folder_path, exist_ok=True)
        response = requests.get(url=song_info["header_image_thumbnail_url"])
        response.raise_for_status()

        filename = f"{song_info["title"]}.png"
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)


def download_text(songs):
    for song_info in songs:
        url = song_info["relationships_index_url"]
        response = requests.get(url)
        response.raise_for_status()
        bs = BeautifulSoup(response.text, 'html.parser')
        temp = bs.select_one('.Lyrics__Container-sc-68a46031-1')
        if hasattr(temp, 'select_one'):
            temp.select_one('.LyricsHeader__Container-sc-6f4ef545-1').decompose()
            text_music = temp.get_text(separator='\n')

            folder_path = f"songs/{song_info["artist_names"]}/lirycs/"
            os.makedirs(folder_path, exist_ok=True)
            filename = f"{song_info["title"]}.txt"
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(text_music)