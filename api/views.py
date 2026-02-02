from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer, AttendanceSerializer
from .models import Attendance


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


@api_view(["POST"])
def attendance_summary(request):
    from_date, to_date= request.data["from_date"], request.data["to_date"]
    employees = Employee.objects.prefetch_related("attendance_records")
    summary = []
    for employee in employees:
        records = employee.attendance_records.filter(date__range=[from_date, to_date])
        summary.append({
            "id":employee.id,
            "employee_id": employee.employee_id,
            "name": employee.name,
            "total_present": records.filter(status="Present").count(),
            "total_absent": records.filter(status="Absent").count(),
        })

    return Response(summary)


@api_view(["POST"])
def attendance_summary_detail(request, id):
    from_date, to_date = request.data["from_date"], request.data["to_date"]
    records = Attendance.objects.filter(employee_id=id,date__range=[from_date, to_date]
        ).order_by("-date").values("date", "status")
    return Response(list(records))

