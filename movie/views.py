import json
from unittest import result

from django.http     import JsonResponse
from django.views    import View 
from movie.models    import *

class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        first_name      = data['first_name']
        last_name       = data['last_name']
        date_of_birth   = data['date_of_birth']
        movie           = data['movies']

        Actor.objects.create(
            first_name      = first_name,
            last_name       = last_name,
            date_of_birth   = date_of_birth,
            movie           = movie
        )
    
        return JsonResponse({'massege' : 'created'} , status = 201)
    def get(self, request):
        actors   = Actor.objects.all()
        results  = []
        for actor in actors:
            if actor in actors
            results.append()



        return JsonResponse({'results' : results } , status = 200)
class MovieView(View):
    def post(self, request):

    
        return JsonResponse({'massege' : 'created'} , status = 201)
    def get(self, request):


        return JsonResponse({'results' : results } , status = 200)
