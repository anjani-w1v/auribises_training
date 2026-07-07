'''
vars 
code segement


sng: tite, artist, duratin, nextsng, prevsng

'''

class song:
    def __init__(self, title, artist, duration):
        self.title=title
        self.artist=artist
        self.duration=duration
        self.next_song=None
        self.prev_song=None

    def show_song(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title:', self.title )
        print('artist:', self.artist )
        print('duration:', self.duration )
        print('Hashcode:', self) 
        print('next_song:', self.next_song )
        print('prev_song:', self.prev_song )
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

song1 = song(
        title='abc', 
        artist='def', 
        duration=3.5)

song2 = song(
        title='pqr', 
        artist='stu', 
        duration=4.5)

song3 = song(
        title='xyz', 
        artist='cc', 
        duration=6.5)



song1.next_song=song2
song2.next_song=song3
song3.next_song=song1

song1.prev_song=song3
song2.prev_song=song1
song3.prev_song=song2

song1.show_song()
song2.show_song()
song.show_song(song3)

song=song1
while True:
    song.show_song()
    song=song.next_song

    if(song==song1):
        break

song=song3
while True:
    song.show_song()
    song=song.next_song

    if(song==song3):
        break




