from django.urls import path
from . import views

app_name = "frontend"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees-list/', views.employees_list, name='employees_list'),
    path('employee-add/', views.employee_add, name='employee_add'),
    path('attendance-mark/', views.attendance_mark, name='attendance_mark'),
    path('attendance-summary/', views.attendance_summary, name='attendance_summary'),
    path('attendance-summary-detail/<int:id>/', views.attendance_summary_detail, name='attendance_summary_detail'),
]

