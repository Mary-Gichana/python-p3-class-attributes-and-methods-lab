class Song:
    genres = []          
    artists = []         
    count = 0            
    genre_count = {}     
    artist_count = {}    

    def __init__(self, name, artist, genre):
        
        self.name = name
        self.artist = artist
        self.genre = genre

        
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.update_genre_count(genre)
        Song.update_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        
        if genre and genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        
        if artist and artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def update_genre_count(cls, genre):
        
        if genre:
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def update_artist_count(cls, artist):
        
        if artist:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
