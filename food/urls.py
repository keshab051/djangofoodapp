from django.urls import path
from . import views
urlpatterns = [
    path("",views.IndexClassView.as_view(),name='index'),       # class based view ko lai ra class based view ma .as view garna jaruri xa
    # path("",views.IndexClassView.as_view(),name='index'),      funtion based view ko lai 
    path('item/',views.item,name='item'),
    path('<int:item_id>/',views.detail,name='detail'),
    # for adding item from website insted of admin pannel
    path('add/',views.create_item,name='create_item'),
    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    # delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),

    ]