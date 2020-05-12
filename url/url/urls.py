from django.contrib import admin
from django.urls import path
from url import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name='hi',),
    path('hello/',views.hello,name='hello',),
    path('rollno/<int:id>',views.rollno,name='rollno'),
    path('st/<str:ld>',views.st,name='st'),

]
