from tinytag import TinyTag
import os
import getpass

default_path =  f"C:\\Users\\{getpass.getuser()}\\Music"

def get_musics(path:str =default_path):
    musics = []
    for item in os.listdir(path):
        if not os.path.isdir(item) and ".mp3" in item: 
            musics.append(os.path.join(path, item))

    return musics


def get_metadata(path: str):
    music = TinyTag.get(path)
    if len(path.split('/')) == 1 : 
        name = path.split("\\")[-1].split(".mp3")[0]
    else:
        name = path.split("/")[-1].split(".mp3")[0]
    return {
        "path": path,
        "name": str(name),
        "title":    music.title if music.title != None else "---",
        "artist":   music.artist if music.artist != None else "---",
        "release":  music.year if music.year != None else "---",
        "album":    music.album if music.album else "---",
        "duration": str(int(music.duration//60))+":"+str(int(music.duration%60))
    }

