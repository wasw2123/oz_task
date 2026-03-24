"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import todo.views
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo.views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', todo.views.todo_info, name='todo_info'),
    path('todo/create/', todo.views.todo_create, name='todo_create'),
    path('todo/<int:pk>/update/', todo.views.todo_update, name='todo_update'),
    path('todo/<int:pk>/delete/', todo.views.todo_delete, name='todo_delete'),
    path('cbv/', include('todo.urls')),



    # auth
    path('signup/', users.views.sign_up, name='sign_up' ),
    path('login/', users.views.user_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),

    # utils
    path('summernote/', include('django_summernote.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)