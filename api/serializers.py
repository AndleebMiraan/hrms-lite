from rest_framework.serializers import ModelSerializer, CharField
from .models import Employee, Attendance
from rest_framework.validators import UniqueTogetherValidator

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class AttendanceSerializer(ModelSerializer):
    employee_name = CharField(source="employee.name", read_only=True)

    class Meta:
        model = Attendance
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Attendance.objects.all(),
                fields=["employee", "date"],
                message="Attendance for this employee on this date already exists."
            )
        ]

