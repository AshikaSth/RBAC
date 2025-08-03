from django.urls import path
from .views import *
urlpatterns = [
    path("admin-panel/", AdminPanelView.as_view(), name="admin-view"),
    path("customer-view/", UserView.as_view(), name="user-view"),

  ]