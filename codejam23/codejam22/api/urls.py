from django.urls import path
from . import views

urlpatterns = [
    path("get/listing/<id>", views.getListing, name="allListing"),
    path("add/listing", views.createListing),
    path("update/listing/<int:id>", views.updateListing),
    path("delete/listing/<int:id>", views.deleteListing),
    path("sendRequest/", views.sendRequest),
]
