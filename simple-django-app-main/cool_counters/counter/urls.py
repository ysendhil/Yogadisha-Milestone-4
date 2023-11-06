
from django.urls import path
from . import views

urlpatterns = [
    path('CNIT581-048-Milestone3', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('add_item/', views.add_item, name='add_item'),  # Add this line for adding a record
    path('chatbot/', views.chatbot, name='chatbot'),
]

