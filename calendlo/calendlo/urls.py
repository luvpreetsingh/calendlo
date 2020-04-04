# django level imports
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter

# intialize DefaultRouter
router = SimpleRouter()

# import views
from accounts import views as accounts_views

# register app urls with router
router.register(r'accounts', accounts_views.CalendloUserViewSet, basename='accounts')

urlpatterns = [
    path('api/v1/', include((router.urls, 'api'))),
    path('HM9BQ2/calendlo/admin/', admin.site.urls),
]
