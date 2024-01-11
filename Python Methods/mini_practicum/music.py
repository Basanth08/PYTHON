class Time:
    __slots__ = ['hours', 'minutes', 'seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Song:
    __slots__ = ['title', 'artist', 'Time']

    def __init__(self, title, artist, Time):
        self.title = title
        self.artist = artist
        self.Time = Time

class Album:
    __slots__ = ['title', 'artists', 'tracks', 'length']

    def __init__(self, title, artists):
        self.title = title
        self.artists = artists
        self.tracks = []  # Initialize tracks as an empty list
        self.length = Time(0, 0, 0)

    def add_song(self, song):
        self.tracks.append(song)
        self.length.hours += song.Time.hours
        self.length.minutes += song.Time.minutes
        self.length.seconds += song.Time.seconds

        if self.length.seconds >= 60:
            self.length.seconds -= 60
            self.length.minutes += 1
        if self.length.minutes >= 60:
            self.length.minutes -= 60
            self.length.hours += 1

    def get_time(self, time):
        return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)

    def print_album(self):
        print(self.title + " by " + ', '.join(self.artists))  # Join artists into a string
        for track in self.tracks:
            print(track.title, "-", track.artist, self.get_time(track.Time))

def main():
    song1 = Song("Track 1", "Artist 1", Time(0, 3, 45))
    song2 = Song("Track 2", "Artist 2", Time(0, 5, 30))
    album = Album("My Album", ["Artist 1", "Artist 2"])
    album.add_song(song1)
    album.add_song(song2)
    album.print_album()

if __name__ == "__main__":
    main()
