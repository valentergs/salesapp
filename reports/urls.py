from django.urls import path, re_path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.ReportsListView.as_view(), name='list'),
    path('new/', views.ReportsCreateView.as_view(), name='create'),
    path('by/<username>/<int:pk>/', views.ReportsDetailView.as_view(), name='details'),
    path('create/', views.ReportsCreateView.as_view(), name='create'),
    path('update/by/<username>/<int:pk>', views.ReportsUpdateView.as_view(), name='update'),
    path('delete/by/<username>/<int:pk>', views.ReportsDeleteView.as_view(), name='delete'),
]
