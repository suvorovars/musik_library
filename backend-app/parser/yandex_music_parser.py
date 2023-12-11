from yandex_music import Client
import pandas as pd
import environ

'''
Эта функция получает на вход:
client: объект класса Client, с помощью которого будет осуществляться обращение по API
query: имя исполнителя
num_of_tracks: количество треков, которые необходимо достать

Эта функция отправляет запрос к поисковой строке Yandex Music, выбирает самый первый результат. После чего достаёт необходимое количество треков самого подходящего под query артиста. 
'''
def search_artists(client: Client, query: str,  num_of_tracks: int = 5) -> dict:
    strings = []
    search_output = client.search(query).best

    artist_id = search_output.result.id
    artist_name = search_output.result.name
    strings.extend(get_tracks(client, artist_id, artist_name, num_of_tracks)) 

    return strings

'''
Эта функция получает на вход:
client: объект класса Client, с помощью которого будет осуществляться обращение по API
artist_id: id исполнителя
artist_name: псевдоним исполнителя
num_of_tracks: количество треков, которые необходимо достать

Эта функция получает N лучших треков исполнителя и возвращает список из artist_id, имени исполнителя, track_id, названии песни и жанра.
'''
def get_tracks(client: Client, artist_id: int, artist_name: int, num_of_tracks: int) -> list:
    template = {'artist_id':None, 'artist_name': None, 'track_id': None, 'track_title': None, 'genre': None}
    tracks_info = []
    c = 0
    for track_info in client.artists_tracks(artist_id).tracks:
        template['artist_id'] = artist_id
        template['artist_name'] = artist_name
        template['track_id'] = int(track_info.id)
        template['track_title'] = track_info.title
        template['genre'] = track_info.albums[0].genre
        tracks_info.append(template.copy())
        if c == num_of_tracks:
            break
        c += 1
    return tracks_info

def get_client(path=".env") -> Client:
    env = environ.Env(DEBUG=(bool, False))
    environ.Env.read_env()
    client = Client(token=env("TOKEN"))
    client.init()
    return client

        
def main():
    env = environ.Env(DEBUG=(bool, False))
    environ.Env.read_env()
    client = Client(token=env("TOKEN"))
    client.init()

    columns = ['artist_id', 'artist_name', 'track_id', 'track_title', 'genre']
    df = pd.DataFrame(columns=columns)

    #Получить 5 самых популярных трека BONES
    artist = search_artists(client, "BONES", 5)
    df = df._append(artist, ignore_index=True)
    df.to_csv("data.csv", index=False)

if __name__ == '__main__':
    main()