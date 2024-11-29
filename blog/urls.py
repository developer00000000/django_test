from django.urls import path
from .views import index_view, home_view, staff_view, add_staff_view
from . import views

urlpatterns = [
    path("", home_view, name="home"),
    path("staff/<int:id>/", staff_view, name="staff" ),
    path("index/", index_view, name="index"),
    path("delete/<int:id>/", views.delete_item, name='delete_item'),
    path("edit/<int:id>/", views.edit_item, name='edit_item'),
    path("staff/add/", add_staff_view, name="add_staff")
]