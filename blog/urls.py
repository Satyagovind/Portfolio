from django.conf.urls.static import static
from django.conf import settings
from blog import views
from django.urls import path
from django.contrib import admin

app_name = 'Blogs'

urlpatterns = [
#     path('admin/', admin.site.urls),
    path('',views.some,name='all_blogs'),
    path('<int:blog_id>/',views.details,name='details'),
]