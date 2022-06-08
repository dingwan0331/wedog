from django.urls    import path
from movie.views    import *

urlpartterns = [
    path(''        , ActorView.as_view()),
    path('/actor'  , ActorView.as_view()),
    path('/movie'  , MovieView.as_view())
]