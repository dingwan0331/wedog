import json
from unittest import result

from django.http    import JsonResponse
from django.views   import View
from owner.models   import *

class OwnerView(View):
    def post(self, request):
        data    = json.loads(request.body)
        name    = data['name']
        email   = data['email']
        age     = data['age']
        Owner.objects.create(
            name    = name , 
            email   = email , 
            age     = age ,
        )
        return JsonResponse({'message' : 'created'} , status = 201)

    def get(self, request):
        owners      = Owner.objects.all()
        results     = []

        for owner in owners:
            results.append(
                {
                    "email" : owner.email ,
                    "age"   : owner.age ,
                    "name"  : owner.name 
                }
            )
        return JsonResponse({'results' : results}, status = 200)

class DogView(View):
    def post(self, request):
        data        = json.loads(request.body)
        owner       = Owner.objects.get(name=data['owner'])
        name        = data['name']
        age         = data['age']

        Dog.objects.create(
            name    = name ,
            owner   = owner ,
            age     = age 
        )

        return JsonResponse({'message' : 'created'} , status = 201)

    def get(self, request):
        dogs      = Dog.objects.all()
        results     = []

        for dog in dogs:
            results.append(
                {
                    "owner" : Owner.objects.get(id = dog.owner_id).name ,
                    "age"   : dog.age ,
                    "name"  : dog.name 
                }
            )
        return JsonResponse({'results' : results}, status = 200)