from django.shortcuts import render, redirect
from main_page.models import BookATable, ContactUs, Dish, Category
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_list(request):
    lst = BookATable.objects.filter(is_processed=False)

    return render(request, 'reservation_list.html', context={'lst': lst,
                                                             })


@login_required(login_url='/login/')
def update_reservation(request, pk):
    BookATable.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservation_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contact_lst(request):
    contactlst = ContactUs.objects.filter(is_processed=False)

    return render(request, 'contac_us.html', context={'contact_lst': contactlst})


@login_required(login_url='/login/')
def update_contact(request, pk):
    ContactUs.objects.filter(pk=pk).update(is_processed=True)

    return redirect('manager:contact_lst')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def dish_lst(request):
    dish_lst = Dish.objects.all

    return render(request, 'dishes.html', context={'dish_lst': dish_lst})


@login_required(login_url='/login/')
def update_dish(request, pk):
    if Dish.objects.filter(pk=pk).filter(is_visible=True):
        Dish.objects.filter(pk=pk).update(is_visible=False)
    else:
        Dish.objects.filter(pk=pk).update(is_visible=True)
    return redirect('manager:dish_lst')
