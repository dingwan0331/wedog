from django.urls    import path
from my_movie.views    import *

urlpatterns = [
    path(''        , ActorView.as_view()),
    path('/actor'  , ActorView.as_view()),
    path('/movie'  , MovieView.as_view())
]