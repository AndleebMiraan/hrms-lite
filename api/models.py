from django.db.models import Model, CharField, DateField, ForeignKey, CASCADE,UniqueConstraint, EmailField

STATUS_CHOICES = [("Present", "Present"), ("Absent", "Absent")]

class Employee(Model):
    employee_id = CharField(max_length=20, unique=True)
    name = CharField(max_length=100)
    email = EmailField(max_length=100, unique=True)
    department = CharField(max_length=50)

    def __str__(self): return self.name

    class Meta:
        db_table = "employee"
        verbose_name_plural = "employees"


class Attendance(Model):
    employee = ForeignKey(Employee, on_delete=CASCADE, related_name="attendance_records")
    date = DateField()
    status = CharField(max_length=7, choices=[("Present","Present"),("Absent","Absent")])

    def __str__(self): return f"{self.employee.name} - {self.date} - {self.status}"

    class Meta:
        db_table = "attendance"
        verbose_name_plural = "attendances"
        constraints = [UniqueConstraint(fields=["employee", "date"], name="unique_employee_date")]

