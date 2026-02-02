from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, attendance_summary, attendance_summary_detail

app_name = "api"

router = DefaultRouter()
router.register("employee", EmployeeViewSet)
router.register("attendance", AttendanceViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("attendance-summary", attendance_summary, name="attendance-summary"),
    path("attendance-summary-detail/<int:id>/", attendance_summary_detail, name="attendance-summary-detail"),
]
