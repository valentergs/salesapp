from django.urls import path, re_path
from salesapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home', views.home, name='index'),
    path('customers/', views.CustomersListView.as_view(), name='url_cust_list'),
    # re_path(r'^(?P<pk>[-\w]+)/$', views.CustomersDetailView.as_view(), name='url_cust_detail'),
    path('customers/<int:pk>/', views.CustomersDetailView.as_view(), name='url_cust_detail'),
    path('customers/update/<int:pk>/', views.CustomersUpdateView.as_view(), name='url_cust_update'),

    # Registration urls
    path('password_reset', auth_views.password_reset, name='password_reset'),
    path('password_reset_done', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete', auth_views.password_reset_complete, name='password_reset_complete'),
    path('logout/', views.user_logout, name='logout'),
]
