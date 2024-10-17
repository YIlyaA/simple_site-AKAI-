from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('search/', views.IndexView.as_view(), name="search"),
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.AddIndexView.as_view(), name='add_record'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
    path('<int:pk>/', views.SingleIndexView.as_view(), name='single_index'),
]