import re
f = open("Pink_Floyd_DB.txt", "r")
file = f.readlines()

AlbumsDict = {}
SongsDict = {}
albums = []
Songs = []
for line in file:
    if line.startswith("#"):
        albums.append(line)
    if line.startswith("*"):
        Songs.append(line)


def getAlbums():
    for line in file:
        if line.startswith("#"):
            print(line.strip())


def songs_in_album(album_name):
    printing = False
    index = albums.index(album_name)
    songs = []
    for line in file:
        if line.startswith(album_name):
            printing = True
        elif line.startswith(albums[index - 1]):
            printing = False
        if printing:
            if line.startswith('*'):
                songs.append(line)
    return songs


def getWords(songs_name):
    printing = False
    index = Songs.index(songs_name)
    x = index + 1
    if x == len(Songs):
        x = index
    words = []
    for line in file:
        if line.startswith(songs_name):
            printing = True
        elif line.startswith(Songs[x]):
            printing = False
        if printing:
            if not line.startswith('*') and not line.startswith('#'):
                words.append(line)
    return ''.join(words)


def createAlbumsDict():
    for line in file:
        if line.startswith('#'):
            AlbumsDict[line[:-7]] = songs_in_album(line)


def createSongsDict():
    for line in file:
        if line.startswith('*'):
            SongsDict[line] = getWords(line)


createAlbumsDict()
createSongsDict()


def getTimeOfSong(song):
    for i in Songs:
        if i.startswith(song):
            list_time_of_song = list(map(int, re.findall('\d+', i)))
            str_time_of_song = ':'.join(str(e) for e in list_time_of_song)
            return (str_time_of_song)


print(SongsDict)
# //song = (list(SongsDict.keys())[0])
# print(x)
# list_time_of_song = list(map(int, re.findall('\d+', song)))
# str_time_of_song = ':'.join(str(e) for e in list_time_of_song)
# print(str_time_of_song)
input_number = int(input("enter number: "))
while input_number < 8:
    if input_number == 1:
        getAlbums()
        break

    elif input_number == 2:
        album_name = input("enter name of album: ")
        print(AlbumsDict['#' + album_name])
        break

    elif input_number == 3:
        song_name = input("enter name of song: ")
        print(getTimeOfSong('*' + song_name))
        break
    elif input_number == 4:
        song_name = input("enter name of song: ")
        for i in SongsDict:
            if i.startswith('*' + song_name):
                print(SongsDict[i])
        break
    elif input_number == 5:
        song_name = input("enter name of song: ")
        for i in SongsDict:
            if i.startswith('*' + song_name):
                print(SongsDict[i])
        break
