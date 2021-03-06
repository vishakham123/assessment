from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path("view/", listView, name="petient-list"),
    path("add/", create_petient, name="petient-create"),
    path("edit/<int:pk>/", edit_petient, name="petient-edit"),
    path("details/<int:pk>/", customer_details, name="petient-details"),
    path("delete/<int:pk>/", delete_petient, name="petient-delete"),

    path("ajax_form", ajax_form, name= "ajax-form"),
    path("list/", userList, name="list"),
]