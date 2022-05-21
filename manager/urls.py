from django.urls import path
from .views import reservation_list, update_reservation, contact_lst, update_contact, dish_lst, update_dish

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reservation'),
    path('contact/', contact_lst, name='contact_lst'),
    path('contact/update/<int:pk>/', update_contact, name='update_contact'),
    path('dishes/', dish_lst, name='dish_lst'),
    path('dishes/update/<int:pk>/', update_dish, name='update_dish'),
]
