from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about-page'),
    path('profile', views.UserProfile, name='profile-page'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('products', views.products, name='products'),
    path('customer/<str:pk>', views.customers, name='customer'),
    path('createorder/<str:pk>', views.CreateOrder, name='createorder'),
    path('updateorder/<str:pk>', views.UpdateOrder, name='updateorder'),
    path('deleteorder/<str:pk>', views.DeleteOrder, name='deleteorder'),
    path('registration', views.UserRegistration, name='registration'),
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)