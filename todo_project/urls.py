from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from todo_app.views import TodoItemViewSet

router = routers.DefaultRouter()
router.register(r'todo-items', TodoItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/')),  # Redirect to the API path
]
