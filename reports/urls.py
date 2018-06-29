from django.urls import path, re_path
from reports.views import (ReportsListView, 
                            ReportsDetailView, 
                            ReportsCreateView, 
                            ReportsUpdateView, 
                            ReportsDeleteView)

app_name = 'reports'

urlpatterns = [
    path('', ReportsListView.as_view(), name='list'),
    path('details/<username>/<int:pk>/', ReportsDetailView.as_view(), name='details'),
    path('create/', ReportsCreateView.as_view(), name='create'),
    path('details/<username>/<int:pk>/update/', ReportsUpdateView.as_view(), name='update'),
    path('delete/by/<username>/<int:pk>', ReportsDeleteView.as_view(), name='delete'),
]
