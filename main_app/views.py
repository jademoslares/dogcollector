from django.shortcuts import render

from .models import Dog

dogs = [
  {'name': 'Itsuki', 'breed': 'Husky', 'description': 'Elegant and proud', 'age': 3},
  {'name': 'Hisui', 'breed': 'Shiba Inu', 'description': 'Smart and Energetic', 'age': 2},
]
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogsDatabase = Dog.objects.all()
  return render(request, 'dogs/index.html', {'dogs': dogsDatabase})

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', {'dog': dog})