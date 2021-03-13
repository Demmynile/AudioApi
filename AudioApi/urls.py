from django.urls import path
from .views import AudioBookList , AudioBookCreate, AudioBookRetrieve, AudioBookDelete,AudioBookUpdate


urlpatterns = [
    path('' , AudioBookList.as_view()),
    path('create' , AudioBookCreate.as_view()),
    path('<pk>' , AudioBookRetrieve.as_view()),
    path('delete/<pk>/' , AudioBookDelete.as_view()),
    path('update/<pk>/' , AudioBookUpdate.as_view()),
]
