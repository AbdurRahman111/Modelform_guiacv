
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('submit_form', views.submit_form, name='submit_form'),
    path('see_all', views.see_all, name='see_all'),
    path('details_person/<int:pk>', views.details_person, name='details_person'),
    path('edit_person/<int:pk>', views.edit_person, name='edit_person'),
    path('delete_person/<int:pk>', views.delete_person, name='delete_person'),
]
