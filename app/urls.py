# from django.urls import path
# from . import views 
# from .views import home, add

# urlpatterns = [
#     path('', views.home),
#     path('add', add),
#     # path('add/', views.add, name='add')
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('home/', views.home),
    path('blog/', views.blog),
    path('about/', views.about),
    path('contract/', views.contract)
]


