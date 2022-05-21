from django.shortcuts import render, redirect
from .models import Category, Dish, WhyUs,\
    Events, Chefs, Testimonials, Gallery
import random
from .forms import BookATableForm, ContactUsForm


def main_page(request):
    if request.method == 'POST':
        bookatable = BookATableForm(request.POST)
        contactus = ContactUsForm(request.POST)
        if bookatable.is_valid():
            bookatable.save()
            return redirect('/')
        if contactus.is_valid():
            contactus.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible=True).order_by('position')
    special = Dish.objects.filter(is_visible=True, is_special=True).order_by('position')
    whyus = WhyUs.objects.filter(is_visible=True).order_by('number')
    events = Events.objects.filter(is_visible=True).order_by('position')
    chefs = Chefs.objects.filter(is_visible=True).order_by('position')
    testimonials = Testimonials.objects.filter(is_visible=True).order_by('position')
    gallery = list(Gallery.objects.filter(is_visible=True).order_by('number'))
    random.shuffle(gallery)
    bookatable = BookATableForm()
    contactus = ContactUsForm()

    return render(request, 'main.html', context={'categories': categories,
                                                 'dishes': dishes,
                                                 'special': special,
                                                 'whyus': whyus,
                                                 'events': events,
                                                 'chefs': chefs,
                                                 'testimonials': testimonials,
                                                 'gallery': gallery,
                                                 'bookatable': bookatable,
                                                 'contactus': contactus,
                                                 })
