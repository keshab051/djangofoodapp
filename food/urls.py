from django.urls import path
from . import views
urlpatterns = [
    path("",views.IndexClassView.as_view(),name='index'),       # class based view ko lai ra class based view ma .as view garna jaruri xa
    # path("",views.IndexClassView.as_view(),name='index'),      funtion based view ko lai 
    path('item/',views.item,name='item'),

    # using detail function based view
    # path('<int:item_id>/',views.detail,name='detail'),

    # using detail class based view
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),

    # for adding item from website insted of admin pannel
   
    # url for function based create view
    # path('add/',views.create_item,name='create_item'),
   
    # url for class based create view 
    path('add/',views.CreateItem.as_view(),name='create_item'),

    # edit
    path('update/<int:id>/',views.update_item,name='update_item'),

    # delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),

    ]