from django.urls import path
from . import views

urlpatterns = [
    path('stall', views.index_stall),
    path('stall/create', views.create_stall),
    path('stall/store', views.store_stall),
    path('stall/show/<int:stall_id>', views.show_stall),
    path('stall/edit/<int:stall_id>', views.edit_stall),
    path('stall/update/<int:stall_id>', views.update_stall),
    path('stall/delete/<int:stall_id>', views.delete_stall),
    path('stall/destroy/<int:stall_id>', views.destroy_stall),
    
    path('user', views.index_user),
    path('user/create', views.create_user),
    path('user/store', views.store_user)
]
