"""untitled5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from Blog import views
from django.conf.urls.static import static

from Users.views import MyLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<int:pk>/',views.BlogDetailView.as_view()),
    path('blog/', views.BlogView.as_view(), name='blogs'),
    path('Users/', include('Users.urls')),
    path('accounts/', include('allauth.urls')),
    path('today/', views.saw_date),
    path('image/', views.image_view),
    path('createpost/', views.create_post),
    path('students/', views.student_view),
    path('accounts/login/',MyLoginView.as_view()),
    path('blog-data/', views.BlogListApiView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
