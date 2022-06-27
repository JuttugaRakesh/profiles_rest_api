from django.urls import path, include
from profile_app import views
urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
]
