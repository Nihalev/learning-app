"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup', views.signup),
    path('login', views.signin),
    path('logout', views.signout),
    path('class/<int:value>/',views.classes),
    path('userdetails',views.userdetails),
    path('addbook',views.addbook),
    path('all_classes',views.all_classes),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
