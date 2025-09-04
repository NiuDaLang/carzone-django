from django.shortcuts import render
from .models import Car


# Create your views here.
def cars(request):
  # cars = Car.objects.all().filter()
  return render(request, "cars/cars.html")