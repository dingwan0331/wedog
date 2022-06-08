import json
from unittest import result

from django.http     import JsonResponse
from django.views    import View 
from my_movie.models    import *

class ActorView(View):

    def get(self, request):
        actors   = Actor.objects.all()
        results  = []

        for actor in actors:
            results.append({
                    'first_name'    : actor.first_name,
                    'last_name'     : actor.last_name,
                    'date_of_birth' : actor.date_of_birth,
                    'movie'         : 
                    [movie.title for movie in actor.movies.all()]
                }
            )
        return JsonResponse({'results' : results } , status = 200)

class MovieView(View):
    
    def get(self, request):
        movies   = Movie.objects.all()
        results  = []
        for movie in movies:
            results.append({
                'release_date'  : movie.release_date ,
                'running_time'  : movie.running_time ,
                'title'         : movie.title ,
                'actors'        : 
                [actor.last_name + actor.first_name for actor in movie.actor_set.all()]
            })

        return JsonResponse({'results' : results } , status = 200)



    # def post(self, request):
    #     data = json.loads(request.body)
    #     first_name      = data['first_name']
    #     last_name       = data['last_name']
    #     date_of_birth   = data['date_of_birth']
    #     movie           = data['movies']
        
    #     Actor.objects.create(
    #         first_name      = first_name,
    #         last_name       = last_name,
    #         date_of_birth   = date_of_birth,
    #         movie           = movie
    #     )
    
    #     return JsonResponse({'massege' : 'created'} , status = 201)