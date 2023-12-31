
from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:mov_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('add_new/',views.add_new,name='add_new'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
