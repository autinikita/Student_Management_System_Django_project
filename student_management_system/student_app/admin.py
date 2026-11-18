# from django.contrib import admin
# from.models import Student, Role, Roll_Number, Department


# # Register your models here.
# admin.site.register(Student)
# admin.site.register(Role)
# admin.site.register(Department)
# admin.site.register(Roll_Number)





from django.contrib import admin
from .models import Department, Role, Grade, Roll_Number, Student

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Grade)
admin.site.register(Roll_Number)
admin.site.register(Student)