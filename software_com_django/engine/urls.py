from django.urls import path
from .views import senny_brain

urlpatterns = [
    path("api/", senny_brain, name="senny_dispatcher"),
]
