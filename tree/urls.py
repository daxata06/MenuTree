from django.urls import path

from .views import index

urlpatterns = [
    path("", index, name="index"),
    path("<slug>/", index, name="index"),
    path("<slug>/<path:url>/", index, name="index"),
]
