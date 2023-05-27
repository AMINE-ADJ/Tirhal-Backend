from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='to register user'),
    path('login/',views.login, name='to login user'),
    path('addregion/',views.addregion, name='to add region and assign it to an admin'),
    path('placeinregion/<int:id>',views.getAllPlaceInRegion,name=''),
    path('place/<int:id>',views.getPlace,name=''),
    path('favorite/',views.addfavourite,name='to add a place to the favorites'),
    path('myfavorite/<int:id>',views.getfavorite,name='to get favorites of a specific user'),
]