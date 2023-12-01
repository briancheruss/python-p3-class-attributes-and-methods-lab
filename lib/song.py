class Song:
    pass
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment count and add song to genres and artists
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artist_count(self.artist)

    def add_song_to_count(self):
        Song.count += 1

    def add_to_genres(self, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)

    def add_to_artists(self, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)

    def add_to_genre_count(self, genre):
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

    def add_to_artist_count(self, artist):
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
