from django.shortcuts import render
from api.models import Employee, Attendance
from django.db.models import Min, Max
from django.utils.timezone import now


def dashboard(request):
    today = now().date()
    total_employees = Employee.objects.count()
    present_today = Attendance.objects.filter(date=today, status="Present").count()
    absent_today = Attendance.objects.filter(date=today, status="Absent").count()

    return render(request, "dashboard.html", {
        "total_employees": total_employees,
        "present_today": present_today,
        "absent_today": absent_today,
    })

def employees_list(request):
    all_employees = Employee.objects.all().order_by("name")
    return render(request, "employees_list.html", {"objects": all_employees,})

def employee_add(request):
    return render(request, "employee_add.html",{})

def attendance_mark(request):
    employees = Employee.objects.all().order_by("name")
    return render(request, "attendance_mark.html", {"employees": employees,})

def attendance_summary(request):
    dates = Attendance.objects.aggregate(min_date=Min("date"), max_date=Max("date"))
    return render(request, "attendance_summary.html", {
        "min_date": dates["min_date"].strftime("%Y-%m-%d") if dates["min_date"] else "",
        "max_date": dates["max_date"].strftime("%Y-%m-%d") if dates["max_date"] else "",
    })
    
def attendance_summary_detail(request, id):
    employee = Employee.objects.get(id=id)
    dates = Attendance.objects.filter(employee=employee).aggregate(min_date=Min("date"),max_date=Max("date")
    )
    return render(request, "attendance_summary_detail.html", {
        "employee": employee,
        "min_date": dates["min_date"].strftime("%Y-%m-%d") if dates["min_date"] else "",
        "max_date": dates["max_date"].strftime("%Y-%m-%d") if dates["max_date"] else "",
    })



