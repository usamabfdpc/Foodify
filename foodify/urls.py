from django.urls import path
from .import views

urlpatterns = [
    path("displayCategoryList",views.change_category_display,name='display-category-list'),
    path("deleteCategoryList",views.delete_category_display,name="delete-category-list")
]
