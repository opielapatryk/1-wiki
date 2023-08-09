from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.title, name="title"),
    path("search",views.query, name="query"),
    path("create",views.create, name="create"),
]
