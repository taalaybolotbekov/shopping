from django.urls import path
from .views import CategoryCreatApiView, SubcategoryCreatApiView, SubsubcategoriesCreatApiView, LukCreatApiView,\
    LukSingleView


urlpatterns = [
    path('category/', CategoryCreatApiView.as_view()),
    path('subcategory/', SubcategoryCreatApiView.as_view()),
    path('subsubcategory/', SubsubcategoriesCreatApiView.as_view()),
    path('luk/', LukCreatApiView.as_view()),
    path('luk/<int:pk>/', LukSingleView.as_view()),
]