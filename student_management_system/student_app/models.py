# from django.db import models

# # -----------------------
# # Department
# # -----------------------
# class Department(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# # -----------------------
# # Role
# # -----------------------
# class Role(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# # -----------------------
# # Roll Number
# # -----------------------
# class Roll_Number(models.Model):
#     roll_no = models.CharField(max_length=30, unique=True)

#     def __str__(self):
#         return self.roll_no


# # -----------------------
# # Student
# # -----------------------
# class Student(models.Model):

#     roll_number = models.ForeignKey(
#         Roll_Number,
#         on_delete=models.CASCADE
#     )

#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

#     marks = models.IntegerField(default=0)

#     grade = models.CharField(max_length=5)

#     phone = models.BigIntegerField()

#     role = models.ForeignKey(
#         Role,
#         on_delete=models.CASCADE
#     )

#     dept = models.ForeignKey(
#         Department,
#         on_delete=models.CASCADE
#     )

#     percentage = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"




from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


class Roll_Number(models.Model):
    roll_no = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.roll_no


class Student(models.Model):
    roll_number = models.ForeignKey(Roll_Number, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    marks = models.IntegerField()
    phone = models.BigIntegerField()
    percentage = models.IntegerField()

    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name