from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# add a flag for
# handling the 404 error
#handler404 = 'core.views.error_404_view'
handler404 = 'core.views.Error_404'
