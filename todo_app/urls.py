from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo_app.views import TodoItemViewSet

router = routers.DefaultRouter()
router.register(r'todo-items', TodoItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
