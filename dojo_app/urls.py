from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('add_book', views.add_book),
    path('<int:book_id>', views.book_info),
    path('<int:book_id>/<int:review_id>/delete', views.delete),
    path('<int:book_id>/add_review', views.add_review),
    path('users/<int:user_id>', views.users),
]
