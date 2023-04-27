import re
f = open("Pink_Floyd_DB - Copy.txt", "r")
file = f.readlines()
f.close()
import pprint
#ןnitialization global vars

AlbumsDict = {}
SongsDict = {}
Albums = []
Songs = []

# initialization func

def createSongsAndAlbums():
    for line in file:
        if line.startswith("#"):
            Albums.append(line)
        if line.startswith("*"):
            Songs.append(line)

def songs_in_album(album_name):
    printing = False
    index = Albums.index(album_name)
    songs = []
    for line in file:
        if line.startswith(album_name):
            printing = True
        elif line.startswith('#') :
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
            AlbumsDict[line] = songs_in_album(line)


def createSongsDict():
    for line in file:
        if line.startswith('*'):
            SongsDict[line] = getWords(line)


createSongsAndAlbums()
createAlbumsDict()
createSongsDict()

# Useful functions


def getAlbums():
    for i in Albums:
        print(i[:-7])

def getSongsInAlbums(album):
    for i in AlbumsDict:
        if album in i:
            print(AlbumsDict[i])

def findAlbumBySong(song):
    song = '*' + song
    for key, value in AlbumsDict.items():
      for i in value:
          if song in i:
              return key

def getTimeOfSong(song):
    song = '*' + song
    for i in Songs:
        if i.startswith(song):
            list_time_of_song = list(map(int, re.findall('\d', i)))
            min = ''.join(str(e) for e in list_time_of_song[0:2])
            sec = ''.join(str(e) for e in list_time_of_song[2:4])
            return (min + ':' + sec)

def getSongLyrics(song):
    song = '*' + song
    for i in SongsDict:
        if i.startswith(song):
            print(SongsDict[i])

def findSongByWord(word):
    for i in SongsDict:
        if word.lower() in i.lower():
            print(i)

def searchWordInSong(word):
    for i in SongsDict:
        if word.lower() in (SongsDict[i]).lower():
            print(i)
print(Songs)

input_number = int(input("enter number: "))
while input_number < 8:
    if input_number == 1:  # Albums List
        getAlbums()
        break

    elif input_number == 2:  # Songs list ly album
        album_name = input("enter name of album: ")
        getSongsInAlbums(album_name)
        break

    elif input_number == 3:  # Song length
        song_name = input("enter name of song: ")
        print(getTimeOfSong(song_name))
        break

    elif input_number == 4:  # Sony lyrics
        song_name = input("enter name of song: ")
        getSongLyrics(song_name)
        break

    elif input_number == 5:  # What album is the song on?
        song_name = input("enter name of song: ")
        print(findAlbumBySong(song_name))

        break
    elif input_number == 6:  # Find song by word
        word = input("enter word: ")
        print(findSongByWord(word))

        break
    elif input_number == 7:  # Search for a word in a songs lycris
        word = input("enter word: ")
        searchWordInSong(word)

        break
    elif input_number == 8:
        break
