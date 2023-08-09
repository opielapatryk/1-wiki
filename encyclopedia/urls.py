from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry, name="entry"),
    path("search",views.query, name="query"),
    path("create",views.create, name="create"),
    path("edit/<str:title>",views.edit, name="edit"),
    path("random",views.rand, name="random"),
]
