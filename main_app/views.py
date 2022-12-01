from django.shortcuts import render
from django.http import HttpResponse

class Cat: 
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        
    def __str__(self):
        return f"{self.name}"

# create cats
cats = {
    Cat('Rufus', 'tabby', 'crazy, lazy, brazy', 2),
    Cat('Stormy', 'black', 'sweet angel', 3),
    Cat('Duke of Meowington', 'tabby', 'demon', 2),
    Cat('Simba', 'lion', 'brave', 5),
    Cat('Garfield', 'orange tabby', 'loves lasagna', 43),
}

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})
