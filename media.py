import webbrowser

"""Creates a class, Movie, which takes variables for title, storyline,
the URL for poster_image, and the URL for trailer_youtube. It also
defines a method, show_trailer, which opens the URL for trailer_youtube
"""


class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
