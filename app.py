from rich.console import Console
from rich.table import Table
from explorer import get_metadata, get_musics, default_path
from playsound import playsound
from sys import argv

def print_list():
    table = Table(title=f"Musics In {default_path}")

    table.add_column("Code", justify="center", style="red")
    table.add_column("Name", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", justify="center", style="magenta")
    table.add_column("Artist", justify="center", style="green")
    table.add_column("Duration", justify="center", style="green")

    for i in range(len(get_musics())):
        music = get_metadata(get_musics()[i])
        table.add_row(str(i+1), music['name']+"\n", music['title'], music['artist'],music['duration'])

    console = Console()
    console.print(table)

def play(code):
    play(playsound(get_musics()[code-1]["path"]))



if __name__ == "__main__":
    command = argv[1]
    try:
        option = argv[2]
    except:
        pass

    if command == "-l" or command == "--list":
        print_list()
    elif command == "-p" or command == "--play":
        try:
            play(option)
        except:
            print(f"No music by this name \"{option}\"   :(")
