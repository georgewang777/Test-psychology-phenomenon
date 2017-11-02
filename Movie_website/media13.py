import webbrowser
class Movie():
    """create Moive class that store title,storyline,poster url and youtube url!"""
    def __init__(self,movie_title,movie_storyline,
                 poster_image,trailer_youtube):
        """Inits Class with blah."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        #open the trailer link in youtube and show the moive website
        webbrowser.open(self.trailer_youtube_url)
