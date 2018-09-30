from django.urls import path
from . import views

app_name = "transaction"
urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.transaction_list, name="transaction_list"),
    path('add', views.transaction_add, name="transaction_add"),
    path('<int:pk>/', views.transaction_detail, name="transaction_detail"),
    path('<int:pk>/edit', views.transaction_edit, name="transaction_edit"),
    path('<int:pk>/delete', views.transaction_delete, name="transaction_delete"),
]
