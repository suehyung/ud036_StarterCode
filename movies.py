import media
import fresh_tomatoes

# These are instances of class media.Movie, populated with strings for
# title, storyline, poster_image, and trailer_youtube

the_rock = media.Movie(
    "The Rock",
    "Navy SEALs and their crazy hijinks",
    "https://upload.wikimedia.org/wikipedia/en/8/82/The_Rock_%28movie%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=jGVJx5mOtL8"
    )
back_future = media.Movie(
    "Back To The Future",
    "Teenager and his Delorean",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qvsgGtivCgs"
    )
bladerunner = media.Movie(
    "Blade Runner",
    "More human than human",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eogpIG53Cis"
    )
empire = media.Movie(
    "The Empire Strikes Back",
    "Who's your daddy?",
    "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xESiohGGP7g"
    )
dazed = media.Movie(
    "Dazed And Confused",
    "Party time in the 70s",
    "https://upload.wikimedia.org/wikipedia/en/a/af/Dazed_and_Confused_%281993%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Mvj4Ng6yinA"
    )
groundhog = media.Movie(
    "Groundhog Day",
    "Stuck in Punxsutawney, PA",
    "https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=tSVeDx9fk60"
    )

# Creates a list of movie objects
movies = [the_rock, back_future, bladerunner, empire, dazed, groundhog]
# Calls the function that creates and opens in a new tab an HTML file using
# the list of movie objects above
fresh_tomatoes.open_movies_page(movies)
