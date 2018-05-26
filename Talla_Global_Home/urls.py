from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('home/', views.home_page, name = 'home_page'),
    path('features/', views.features, name = 'features'),
    path('licence/', views.licence, name = 'licence'),
    path('deposit/', views.deposit, name = 'deposit&upgrade'),
    path('contact/', views.contact, name = 'contact'),
    path('member_contact/', views.member_contact, name = 'contact'),
    path('cashout/', views.cashout, name = 'memeber_earnings'),
    path('member_home/', views.member_home, name = 'member'),
    path('register/', views.register, name = "register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
