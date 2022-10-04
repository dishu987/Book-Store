from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    path('', views.home, name='home'),
    path('find/q=<str:name>&page=<int:page>', views.find, name='find'),
    path('saved&page=<int:page>',views.saved_books,name="saved_books"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='base/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/',views.RegisterationView.as_view(),name="registration"),
    path('clearRecent&user=<str:username>',views.ClearRecent,name="clear_recent"),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)