class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def show_genres(cls):
        return cls.genres

    @classmethod
    def show_artists(cls):
        return cls.artists

    @classmethod
    def show_genre_count(cls):
        return cls.genre_count

    @classmethod
    def show_artist_count(cls):
        return cls.artist_count


song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Thriller", "Michael Jackson", "Pop")
song3 = Song("Halo", "Beyonce", "Pop")
song4 = Song("Umbrella", "Rihanna", "Pop")
song5 = Song("HUMBLE.", "Kendrick Lamar", "Rap")

print(Song.count)            
print(Song.show_genres())    
print(Song.show_artists())  
print(Song.show_genre_count())   
print(Song.show_artist_count()) 