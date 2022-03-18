from django.urls import path
from . import views

urlpatterns = [

    # http://127.0.0.1:8000/music/index
    path('index',views.index_view),
    path('all_book',views.all_book),
    path('update/<int:id>',views.book_update),
    path('delete',views.book_delete)
    
]
