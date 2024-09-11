from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('create',views.create),
    path('delete/<id>',views.delete),
    path('update/<id>',views.update),
]
