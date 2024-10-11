from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # just testing that the URL routing is working f
from django.http import Http404 # needed for 404 response
from .models import Pet

def home(request):
    return HttpResponse("<h1>This is my home page!</h1>") 


def pet_detail(request, pet_id):
# Response with pet number
    return HttpResponse(F"<h1>Pet Number: {pet_id}")

from .models import Pet
def home(request):
# perform an ORM query to get all pets
    pets = Pet.objects.all()
# call render method defining template to use
# 'home.html and pass pets through as an argument # in a dictionary
    return render(request, 'home.html', {'pets':pets,})

def pet_detail(request, pet_id):
    try:
        # perform an ORM query to get specific pet
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
    # Show an appropriate 404 message
        raise Http404("Pet not found")
    return render(request, 'pet_detail.html', {'pet':pet,})
