# django level imports
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter

# intialize DefaultRouter
router = SimpleRouter()

# import views
from accounts import views as accounts_views
from availability import views as avail_views
from appointments import views as appoint_views

# register app urls with router
router.register(r'accounts', accounts_views.CalendloUserViewSet, basename='accounts')
router.register(r'slots', avail_views.AvailabilitySlotViewSet, basename='slots')
router.register(r'appointments', appoint_views.AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('api/v1/', include((router.urls, 'api'))),
    path('HM9BQ2/calendlo/admin/', admin.site.urls),
]
