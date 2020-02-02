from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
      path("", views.homepage),
      path("res_text", views.res_text),
      path("res_table", views.res_table),
      path("res_image", views.res_image),
      path("res_card", views.res_card),
    ]